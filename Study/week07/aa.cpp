#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>


// Assignment 02


int SCR_WIDTH = 800;
int SCR_HEIGHT = 600;


struct Vertex {
	glm::vec3 Position;
	glm::vec3 Normal;
};

// bunny.obj 파일이 실행 파일과 같은 폴더에 있다고 가정
// --- .obj 파일을 읽어 정점,normal 데이터를 추출(파싱)하는 함수 --- 
bool loadOBJ(const char* path, std::vector<float>& out_data) {
	std::vector<glm::vec3> temp_positions;
	std::vector<glm::vec3> temp_normals;

	std::ifstream file(path);
	if (!file.is_open()) return false;

	std::string line;

	while (std::getline(file, line)) {
		if (line.empty()) continue; // 빈 줄 건너뛰기

		std::stringstream ss(line);
		std::string prefix;
		ss >> prefix;

		if (prefix == "v") {
			glm::vec3 v;
			ss >> v.x >> v.y >> v.z;
			temp_positions.push_back(v);
		}
		else if (prefix == "vn") { // normal
			glm::vec3 n;
			ss >> n.x >> n.y >> n.z;
			temp_normals.push_back(n);
		}
		else if (prefix == "f") {  // face 정보 (v/vt/vn 형태 대응)
			std::string vertexStr;

			// f 뒤에 오는 3개의 값들(예: 1/1/1)을 각각 문자열로 읽음
			for (int i = 0; i < 3; i++) {
				ss >> vertexStr;
				// 문자열에서 첫 번째 숫자(정점 인덱스)만 추출

				size_t firstSlash = vertexStr.find('/');
				size_t lastSlash = vertexStr.find_last_of('/');

				// 1. 위치 인덱스 추출
				int vIdx = std::stoi(vertexStr.substr(0, firstSlash));
				int nIdx = 0; // 우선 초기화로 에러 방지했습니다.


				if (firstSlash != std::string::npos && lastSlash != std::string::npos) {
					// 2. normal 인덱스 추출 (마지막 슬래시 뒤의 숫자)
					nIdx = std::stoi(vertexStr.substr(lastSlash + 1));
				}

				// 인덱스 범위 체크 
				if (vIdx > 0 && vIdx <= (int)temp_positions.size() && nIdx > 0 && nIdx <= (int)temp_normals.size()) {
					glm::vec3 pos = temp_positions[vIdx - 1];
					out_data.push_back(pos.x);
					out_data.push_back(pos.y);
					out_data.push_back(pos.z);

					glm::vec3 norm = temp_normals[nIdx - 1];
					out_data.push_back(norm.x);
					out_data.push_back(norm.y);
					out_data.push_back(norm.z);
				}
			}
		}
	}
	return true;
}



// 셰이더 소스는 이전과 동일하되 색상을 고정값으로 출력하도록 수정
const char* vertexShaderSource = "#version 460 core\n"
"layout (location = 0) in vec3 aPos;\n"
"layout (location = 1) in vec3 aNormal;\n"
"out vec3 Normal;\n"
"out vec3 FragPos;\n"
"uniform mat4 model; uniform mat4 view; uniform mat4 projection;\n"
"uniform mat3 normalMatrix;\n"
"void main() {\n"
// 정점의 월드 공간 좌표 계산
"FragPos = vec3(model * vec4(aPos, 1.0));\n"
// 미리 계산된 노멀 행렬을 사용하여 법선 변환
"Normal = normalMatrix * aNormal;\n"
"gl_Position = projection * view * model * vec4(aPos, 1.0); }\0";



const char* fragmentShaderSource = "#version 460 core\n"
"out vec4 FragColor;\n"
"in vec3 Normal;\n"
"in vec3 FragPos;\n"
"uniform vec3 lightPos; uniform vec3 lightColor; uniform vec3 objectColor;\n"
"void main() { \n"
// 1. Ambient 조명
"float ambientStrength = 0.1;\n"
"vec3 ambient = ambientStrength * lightColor;\n"
// 2. Diffuse 조명
"vec3 norm = normalize(Normal);\n" // normal vector 정규화
"vec3 lightDir = normalize(lightPos - FragPos);\n" // 정점에서 광원을 향하는 방향
"float diff = max(dot(norm, lightDir), 0.0);\n"
"vec3 diffuse = diff * lightColor;\n"
"vec3 result = (ambient + diffuse) * objectColor;\n"
"FragColor = vec4(result, 1.0);\n"
"}\n\0";



void framebuffer_size_callback(GLFWwindow* window, int width, int height) {

	// OpenGL이 그릴 캔버스 영역을 새 창 크기에 맞춤
	glViewport(0, 0, width, height);

	// 전역 변수 업데이트 (렌더링 루프에서 사용)
	SCR_WIDTH = width;
	SCR_HEIGHT = height;
}

// 전역변수와 콜백 함수
// 초기 스케일 값 (1.0 = 100%)
float objectScale = 1.0f;

// 스크롤 감도 (한 번 굴릴 때마다 변하는 정도)
float scaleSensitivity = 0.1f;

void scroll_callback(GLFWwindow* window, double xoffset, double yoffset) {

	// 휠 움직임에 따라 스케일 값 업데이트
	objectScale += (float)yoffset * scaleSensitivity;

	// 물체가 너무 작아져서 사라지거나 뒤집히는 것(음수)을 방지
	if (objectScale < 0.1f)
		objectScale = 0.1f;
}




// 카메라 각도 상태
float yaw = -90.0f; // 초기 시선이 -Z축을 향하도록 설정
float pitch = 0.0f;
float lastX = 800.0f / 2.0; // 화면 중앙
float lastY = 600.0f / 2.0;
bool firstMouse = true;

// 카메라 벡터
glm::vec3 cameraPos = glm::vec3(0.0f, 0.0f, 3.0f);
glm::vec3 cameraFront = glm::vec3(0.0f, 0.0f, -1.0f);
glm::vec3 cameraUp = glm::vec3(0.0f, 1.0f, 0.0f);

// 마우스 이동 콜백 함수
void mouse_callback(GLFWwindow* window, double xposIn, double yposIn) {
	float xpos = static_cast<float>(xposIn);
	float ypos = static_cast<float>(yposIn);
	if (firstMouse) {
		lastX = xpos;
		lastY = ypos;
		firstMouse = false;
	}

	// 마우스 이동량 계산
	float xoffset = xpos - lastX;
	float yoffset = lastY - ypos; // Y축은 위로 갈수록 좌표값이 작아지므로 뒤집음

	lastX = xpos;
	lastY = ypos;

	float sensitivity = 0.1f; // 감도 조절

	xoffset *= sensitivity;
	yoffset *= sensitivity;

	// 2. 오일러 각도 업데이트
	yaw += xoffset;
	pitch += yoffset;

	// 3. Pitch 각도 제한 (90도 이상 꺾여서 화면이 뒤집히는 것 방지)
	if (pitch > 89.0f) pitch = 89.0f;
	if (pitch < -89.0f) pitch = -89.0f;

	// 4. 새로운 방향 벡터 계산 (삼각함수 적용)
	glm::vec3 front;
	front.x = cos(glm::radians(yaw)) * cos(glm::radians(pitch));
	front.y = sin(glm::radians(pitch));
	front.z = sin(glm::radians(yaw)) * cos(glm::radians(pitch));
	cameraFront = glm::normalize(front);

}

// 프레임 간 시간 간격 (이동 속도를 프레임레이트와 무관하게 유지)
float deltaTime = 0.0f;
float lastFrame = 0.0f;


void processInput(GLFWwindow* window) {

	if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_PRESS)
		std::cout << "UP 키 감지됨, cameraPos.z = " << cameraPos.z << std::endl;
	float cameraSpeed = 2.5f * deltaTime; // 이동 속도 (프레임 독립적)

	// yaw 각도만 사용한 수평 전진 방향 벡터 계산 ( Y축 고정)
	glm::vec3 horizontalFront;
	horizontalFront.x = cos(glm::radians(yaw));
	horizontalFront.y = 0.0f;               // 수직 성분 제거 → 바닥에 붙어 이동
	horizontalFront.z = sin(glm::radians(yaw));
	horizontalFront = glm::normalize(horizontalFront);

	// 수평 우측 방향 벡터 (front × up 외적)
	glm::vec3 horizontalRight = glm::normalize(glm::cross(horizontalFront, cameraUp));

	if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_PRESS)    // 전진
		cameraPos += cameraSpeed * horizontalFront;
	if (glfwGetKey(window, GLFW_KEY_DOWN) == GLFW_PRESS)  // 후진
		cameraPos -= cameraSpeed * horizontalFront;
	if (glfwGetKey(window, GLFW_KEY_LEFT) == GLFW_PRESS)  // 좌측 이동
		cameraPos -= cameraSpeed * horizontalRight;
	if (glfwGetKey(window, GLFW_KEY_RIGHT) == GLFW_PRESS) // 우측 이동
		cameraPos += cameraSpeed * horizontalRight;

	if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) // 종료	
		glfwSetWindowShouldClose(window, true);
}



int main() {
	glfwInit();

	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 6);
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE); // 코어 프로파일 사용(권장)

	GLFWwindow* window = glfwCreateWindow(800, 600, "Stanford Bunny", NULL, NULL);

	glfwMakeContextCurrent(window);
	gladLoadGLLoader((GLADloadproc)glfwGetProcAddress);
	glEnable(GL_DEPTH_TEST); // 3D이므로 깊이 테스트

	//glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);
	glfwFocusWindow(window);



	// 셰이더 컴파일 
	unsigned int vertexShader = glCreateShader(GL_VERTEX_SHADER);
	glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
	glCompileShader(vertexShader);

	unsigned int fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
	glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
	glCompileShader(fragmentShader);

	unsigned int shaderProgram = glCreateProgram();
	glAttachShader(shaderProgram, vertexShader);
	glAttachShader(shaderProgram, fragmentShader);
	glLinkProgram(shaderProgram);




	// 데이터 로드 (bunnyData는 [pos.x, pos.y, pos.z, norm.x, norm.y, norm.z, ...] 순서)
	std::vector<float> bunnyData;
	if (!loadOBJ("bunny.obj", bunnyData)) {
		std::cout << "모델 파일을 찾을 수 없습니다!" << std::endl;
		return -1;
	}





	unsigned int VBO, VAO;
	glGenVertexArrays(1, &VAO);
	glGenBuffers(1, &VBO);

	glBindVertexArray(VAO);
	glBindBuffer(GL_ARRAY_BUFFER, VBO);

	glBufferData(GL_ARRAY_BUFFER, bunnyData.size() * sizeof(float), &bunnyData[0], GL_STATIC_DRAW);

	// 1. 위치 속성 (Location 0)
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)0);
	glEnableVertexAttribArray(0);
	// 2. normal 속성 (Location 1) - 시작점 오프셋(3 * float 만큼 띄움)
	glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(3 * sizeof(float)));
	glEnableVertexAttribArray(1);



	// 마우스 커서를 창 안에 가두고 숨김 (FPS 스타일 시점 제어)
	glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);

	// 콜백 함수 등록
	glfwSetFramebufferSizeCallback(window, framebuffer_size_callback); // 창 크기 변경
	glfwSetCursorPosCallback(window, mouse_callback);                 // 마우스 이동
	glfwSetScrollCallback(window, scroll_callback);                    // 스크롤(줌)


	while (!glfwWindowShouldClose(window)) {

		glfwPollEvents();


		float currentFrame = static_cast<float>(glfwGetTime());
		deltaTime = currentFrame - lastFrame;
		lastFrame = currentFrame;

		// 보드 입력 처리 — deltaTime 계산 직후에 호출
		processInput(window);

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		glUseProgram(shaderProgram);

		// 배경색
		glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		// --- MVP 행렬 설정 ---
		// 광원 설정
		glUniform3f(glGetUniformLocation(shaderProgram, "lightPos"), 1.2f, 1.0f, 2.0f);
		glUniform3f(glGetUniformLocation(shaderProgram, "lightColor"), 1.0f, 1.0f, 1.0f);
		glUniform3f(glGetUniformLocation(shaderProgram, "objectColor"), 0.8f, 0.5f, 0.2f);

		// 모델 행렬 생성
		glm::mat4 model = glm::mat4(1.0f);
		model = glm::translate(model, glm::vec3(0.0f, 0.0f, 0.0f));
		//model = glm::rotate(model, (float)glfwGetTime(), glm::vec3(0.0f, 1.0f, 0.0f));

		// 스케일 변환 적용 (X, Y, Z 축 모두 동일한 비율로)
		model = glm::scale(model, glm::vec3(objectScale));


		// 카메라 위치(cameraPos)와 방향(cameraFront)을 이용해 뷰 행렬 생성
		glm::mat4 view = glm::lookAt(cameraPos, cameraPos + cameraFront, cameraUp);

			
		// 새 Aspect Ratio를 반영한 투영 행렬 계산
		float aspect = (float)SCR_WIDTH / (float)SCR_HEIGHT;
		glm::mat4 projection = glm::perspective(glm::radians(45.0f), aspect, 0.1f, 100.0f);
			

		glUniformMatrix4fv(glGetUniformLocation(shaderProgram, "model"), 1, GL_FALSE, glm::value_ptr(model));
		glUniformMatrix4fv(glGetUniformLocation(shaderProgram, "view"), 1, GL_FALSE, glm::value_ptr(view));
		glUniformMatrix4fv(glGetUniformLocation(shaderProgram, "projection"), 1, GL_FALSE, glm::value_ptr(projection));

		// normal 행렬 계산 (CPU에서 한 번만 수행)
		// mat3로 변환하여 역행렬의 전치행렬을 구함
		glm::mat3 normalMatrix = glm::transpose(glm::inverse(glm::mat3(model)));


		// 셰이더로 전달
		unsigned int normalMatLoc = glGetUniformLocation(shaderProgram, "normalMatrix");
		glUniformMatrix3fv(normalMatLoc, 1, GL_FALSE, glm::value_ptr(normalMatrix));
		// 전체 float 개수를 6으로 나눠야 정확한 정점의 개수가 나옴 [x, y, z, nx, ny, nz]
		glDrawArrays(GL_TRIANGLES, 0, bunnyData.size() / 6);


		glfwSwapBuffers(window);
		//glfwPollEvents();
	}
	glfwTerminate();
	return 0;
}


