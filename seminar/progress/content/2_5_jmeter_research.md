## Nghiên cứu chi tiết về Apache JMeter

### Kiến trúc tổng thể của JMeter

Apache JMeter là một công cụ mã nguồn mở được thiết kế để kiểm thử hiệu năng và kiểm thử tải của các ứng dụng web và nhiều loại dịch vụ khác. JMeter có kiến trúc module hóa, sử dụng các thành phần mở rộng (plugin-based) để tổ chức và mô phỏng luồng kiểm thử.

Các thành phần chính trong kiến trúc của JMeter bao gồm:

- **Test Plan**: Cấu trúc gốc của mọi bài kiểm thử, định nghĩa toàn bộ cấu hình và hành vi kiểm thử.
- **Thread Group**: Đại diện cho các người dùng ảo, mô phỏng số lượng lớn người dùng truy cập hệ thống.
- **Samplers**: Gửi các yêu cầu cụ thể đến hệ thống cần kiểm thử.
- **Logic Controllers**: Kiểm soát luồng thực thi trong Thread Group.
- **Listeners**: Ghi nhận và trình bày kết quả kiểm thử.
- **Configuration Elements**: Cung cấp cấu hình mặc định cho các Sampler.
- **Timers**: Tạo độ trễ giữa các yêu cầu.
- **Assertions**: Xác minh kết quả phản hồi có đúng kỳ vọng hay không.
- **Pre/Post-Processors**: Xử lý dữ liệu trước hoặc sau khi gửi yêu cầu.

Các thành phần này có thể được lồng ghép theo cấu trúc phân cấp trong một Test Plan để tạo nên các kịch bản kiểm thử phức tạp.

### Thread Group

Thread Group là đơn vị cấu hình chính để mô phỏng người dùng truy cập hệ thống. Mỗi Thread Group có thể được cấu hình như sau:

- **Number of Threads (users)**: Số lượng người dùng ảo sẽ mô phỏng.
- **Ramp-Up Period (seconds)**: Thời gian để khởi chạy toàn bộ số người dùng ảo.
- **Loop Count**: Số lần mỗi người dùng lặp lại kịch bản kiểm thử.

Thread Group cũng cho phép cấu hình hành vi khi có lỗi (ví dụ: dừng test, bỏ qua sampler,...), đồng thời có thể chứa nhiều thành phần con như Sampler, Timer, Assertions,...

Ví dụ: Nếu cấu hình 50 threads với ramp-up 10 giây và loop count là 2, JMeter sẽ khởi động 5 threads mỗi giây và mỗi người dùng gửi 2 lượt yêu cầu.

### Sampler

Sampler là thành phần chịu trách nhiệm gửi các loại yêu cầu đến hệ thống đang được kiểm thử. Mỗi Sampler tương ứng với một loại giao thức hoặc hành động.

Một số loại Sampler phổ biến:

- **HTTP Request**: Gửi yêu cầu HTTP/HTTPS đến máy chủ web.
- **JDBC Request**: Gửi truy vấn SQL đến hệ quản trị cơ sở dữ liệu thông qua JDBC.
- **FTP Request**: Gửi yêu cầu tải lên hoặc tải về tệp từ máy chủ FTP.
- **SOAP/XML-RPC Request**: Gửi yêu cầu đến các dịch vụ web dựa trên SOAP.
- **Java Request**: Cho phép gọi trực tiếp các class Java do người dùng viết.
- **JMS Request**: Dùng để gửi/nhận message qua hệ thống JMS.

Sampler là yếu tố quan trọng quyết định hệ thống gì đang được kiểm thử và theo cách thức nào.

### Listener

Listener là thành phần giúp thu thập, ghi lại và hiển thị kết quả kiểm thử. Listener có thể ghi log, hiển thị báo cáo theo thời gian thực hoặc lưu vào file để phân tích sau.

Một số Listener tiêu biểu:

- **View Results Tree**: Hiển thị chi tiết từng request và response.
- **Summary Report**: Cung cấp thống kê tổng hợp như số request, thời gian phản hồi trung bình, tỉ lệ lỗi,...
- **Aggregate Report**: Hiển thị thông tin tổng hợp nâng cao như độ lệch chuẩn, tỉ lệ phần trăm thời gian phản hồi,...
- **Graph Results**: Biểu diễn dữ liệu kiểm thử dưới dạng đồ thị.
- **View Results in Table**: Hiển thị danh sách request theo dạng bảng.

Việc lựa chọn Listener phù hợp sẽ giúp việc phân tích hiệu quả hệ thống trở nên trực quan và chính xác hơn.

### Timer, Assertion, Pre-Processor và Post-Processor

1. Timer

Timer được sử dụng để tạo độ trễ giữa các yêu cầu nhằm mô phỏng hành vi người dùng thực tế. Một số loại Timer thường dùng:

- **Constant Timer**: Tạo độ trễ cố định.
- **Uniform Random Timer**: Tạo độ trễ ngẫu nhiên theo phân phối đều.
- **Gaussian Random Timer**: Tạo độ trễ ngẫu nhiên theo phân phối chuẩn.
- **Synchronizing Timer**: Đồng bộ các thread lại với nhau trước khi gửi request.

2. Assertion

Assertion được sử dụng để xác minh rằng phản hồi từ server là đúng và hợp lệ. Một số Assertion thông dụng:

- **Response Assertion**: Kiểm tra nội dung hoặc mã trạng thái phản hồi.
- **Duration Assertion**: Kiểm tra thời gian phản hồi không vượt quá giá trị xác định.
- **Size Assertion**: Kiểm tra kích thước của phản hồi.
- **JSON/XML Assertion**: Kiểm tra cấu trúc và dữ liệu JSON/XML trong phản hồi.

Assertion giúp đánh giá độ chính xác, không chỉ hiệu suất của hệ thống.

3. Pre-Processor

Pre-Processor được thực thi trước khi Sampler được kích hoạt. Nó thường được dùng để:

- Chuẩn bị dữ liệu đầu vào.
- Tạo token, header, hoặc giá trị động.
- Gọi hàm từ BeanShell hoặc JSR223 để xử lý logic tùy chỉnh.

Ví dụ: "User Defined Variables" để thiết lập các giá trị cần dùng cho các request tiếp theo.

4. Post-Processor

Post-Processor được thực thi sau khi Sampler gửi request. Dùng để:

- Trích xuất dữ liệu từ phản hồi để sử dụng ở bước kế tiếp.
- Lưu dữ liệu, ghi log, hoặc xử lý chuỗi phản hồi.
- Phổ biến nhất là **Regular Expression Extractor**, **JSON Extractor**, hoặc **XPath Extractor**.

