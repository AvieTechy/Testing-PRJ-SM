## Research Performance Testing Tools & Compare

### Tổng quan về các công cụ kiểm thử hiệu năng:

#### JMeter

- JMeter là một công cụ kiểm thử hiệu suất mã nguồn mở được phát triển bởi Apache, chủ yếu được sử dụng để kiểm tra độ bền, hiệu suất và khả năng chịu tải của các ứng dụng web, API và máy chủ. Jmeter là một phần mềm mã nguồn mở, được viết bằng Java. Cha đẻ của JMeter là Stefano Mazzocchi. Sau đó Apache đã thiết kế lại để cải tiến hơn giao diện đồ họa cho người dùng và khả năng kiểm thử hướng chức năng. Công cụ hỗ trợ nhiều giao thức như HTTP, FTP, JDBC và SOAP, đồng thời có khả năng mở rộng thông qua các plugin. JMeter phổ biến trong cộng đồng nhờ tính linh hoạt và khả năng mô phỏng hàng nghìn người dùng ảo.

![JMeter](content/images/jmeter.png)

#### k6

- k6 là một công cụ kiểm thử hiệu suất mã nguồn mở, được xây dựng bằng Go và sử dụng JavaScript để viết kịch bản thử nghiệm. Với trọng tâm là đơn giản hóa quy trình kiểm thử cho nhà phát triển, k6 cung cấp giao diện dòng lệnh (CLI) và dễ dàng tích hợp vào pipeline CI/CD. Công cụ này tập trung vào thử nghiệm tải cho API, microservices và ứng dụng web, với ưu điểm là nhẹ, nhanh và hiệu quả về tài nguyên. k6 nổi bật với cộng đồng phát triển mạnh mẽ và tài liệu chi tiết, phù hợp cho các dự án cần tự động hóa và mở rộng quy mô.

![k6](content/images/k6.png)


#### LoadRunner

- LoadRunner là một công cụ kiểm thử hiệu suất thương mại được phát triển bởi Micro Focus, được thiết kế để mô phỏng hàng nghìn người dùng ảo nhằm đánh giá hiệu suất và khả năng chịu tải của các ứng dụng và hệ thống. Công cụ này hỗ trợ nhiều giao thức như HTTP, Web Services, SAP, Oracle, và Citrix, cung cấp khả năng ghi lại và phát lại kịch bản thử nghiệm một cách chi tiết. LoadRunner nổi bật với các tính năng phân tích nâng cao và tích hợp với các công cụ quản lý dự án, nhưng yêu cầu chi phí cấp phép và tài nguyên phần cứng lớn. Nó phù hợp cho các doanh nghiệp cần thử nghiệm quy mô lớn và phân tích chuyên sâu.

![LoadRunner](content/images/loadrunner.png)

#### NeoLoad

- NeoLoad là một công cụ kiểm thử hiệu suất thương mại được phát triển bởi Neotys, tập trung vào việc mô phỏng tải lớn để đánh giá hiệu suất của các ứng dụng web, API và ứng dụng di động. Với giao diện GUI trực quan, NeoLoad hỗ trợ ghi lại và thiết kế kịch bản thử nghiệm dễ dàng, đồng thời cung cấp khả năng phân tán tải qua đám mây. Công cụ này nổi bật với tích hợp mạnh mẽ với CI/CD và báo cáo chi tiết, nhưng yêu cầu chi phí cấp phép. NeoLoad phù hợp cho các doanh nghiệp cần thử nghiệm hiệu suất với quy mô vừa và lớn, đặc biệt trong môi trường DevOps.

![NeoLoad](content/images/neoload.png)

### So sánh chi tiết:

| **Tiêu chí** | **JMeter** | **k6** | **LoadRunner** | **NeoLoad** |
|----------------|----------------|----------------|----------------|----------------|
| **Loại công cụ** | Mã nguồn mở, GUI-based | Mã nguồn mở, CLI-based | Thương mại, GUI và script-based | Thương mại, GUI-based |
| **Hiệu suất** | Tốn tài nguyên, nhưng tối ưu hóa với plugin và phân tán tải lớn | Hiệu suất cao, tối ưu cho tải lớn | Hiệu suất cao, nhưng yêu cầu phần cứng mạnh mẽ | Hiệu suất tốt, tối ưu cho tải phân tán |
| **Hỗ trợ giao thức** | Đa dạng (HTTP, FTP, JDBC, SOAP, v.v.), vượt trội  | Chủ yếu HTTP, WebSocket, gRPC | Rộng (HTTP, Web Services, SAP, Oracle, Citrix), chuyên sâu doanh nghiệp | Hỗ trợ rộng (HTTP, SOAP, REST, v.v.), tập trung chủ yếu vào web và API |
| **Dễ sử dụng** | Dễ với GUI, hỗ trợ tốt với người mới bắt đầu | Dễ với người đã biết JavaScript, khó với người mới bắt đầu | Khó với người mới, cần học cách sử dụng chuyên sâu | Có GUI, nhưng người dùng cần học cách sử dụng |
| **Tích hợp DevOps** | Tích hợp tốt nhưng cần cấu hình thủ công | Tích hợp dễ dàng với CI/CD | Tích hợp mạnh với doanh nghiệp, nhưng phức tạp | Tích hợp tốt với CI/CD, thân thiện |
| **Báo cáo** | Tích hợp sẵn, chi tiết qua GUI và plugin | Tùy chỉnh qua CLI hoặc k6 Cloud | Báo cáo chuyên sâu nhưng có trả phí | Báo cáo chi tiết, tích hợp với các công cụ phân tích |
| **Cộng đồng & plugin** | Lớn, nhiều plugin đa dạng, hỗ trợ mạnh mẽ | Nhỏ hơn, ít plugin hơn | Cộng đồng hạn chế, phụ thuộc hỗ trợ từ Micro Focus | Cộng đồng vừa phải, hỗ trợ từ Neotys |
| **Chi phí** | Hoàn toàn miễn phí, không giới hạn | Miễn phí (local), trả phí cho k6 Cloud | Trả phí cao, yêu cầu cấp phép doanh nghiệp | Trả phí |

→ Lý do chọn JMeter: JMeter nổi bật nhờ tính linh hoạt vượt trội với hỗ trợ đa giao thức, giao diện GUI thân thiện cho người mới, và cộng đồng mã nguồn mở lớn với nhiều plugin miễn phí. JMeter cung cấp giải pháp miễn phí và dễ mở rộng qua phân tán tải, làm cho nó vượt trội trong các dự án có ngân sách hạn chế hoặc yêu cầu linh hoạt cao. Dù có một chút bất lợi hơn về hiệu suất so với các công cụ khác, JMeter bù đắp bằng khả năng cấu hình chi tiết và hỗ trợ đa dạng, phù hợp cho cả người mới và chuyên gia.

\newpage