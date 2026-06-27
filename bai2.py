from fastapi import FastAPI  

app = FastAPI()  
students = [  
    {"id": 1, "name": "An"},  
    {"id": 2, "name": "Binh"},  
    {"id": 3, "name": "Cuong"},  
]  

@app.get("/students")  
def get_all_students():  
    return students

'''
- Endpoint hiện tại trong source code là gì?: http://127.0.0.1:8000/student
- Vì sao khi gọi GET /students lại bị lỗi 404 Not Found? Do ta đang định nghĩa là student nên khi cố gắng gọi GET /students sẽ báo lỗi k tìm thấy
- Vì sao tên endpoint /student chưa phù hợp với yêu cầu lấy danh sách sinh viên? vì đây là dah từ số ít khiến ta dễ hiểu lầm rằng chỉ muốn lấy 1 sinh viên
- Vì sao dòng return students[0] chưa đúng với yêu cầu nghiệp vụ? do bài đang yêu cầu lấy ra danh sách toàn bộ chứ không phải là sinh viên thứ nhất
- API đúng theo yêu cầu khách hàng nên có đường dẫn là gì? Đường dẫn chuẩn xác nhất theo yêu cầu này là: /students
'''
