# Personal Report Template

> Đây là template được dùng có các version pandoc lớn hơn 2.0!

## Cài đặt

Đảm bảo trong máy của bạn có `pandoc` và version `latex`. Nếu đã cài đặt từ trước thì có thể bỏ qua bước này.

### 1. Cài đặt Pandoc
```bash
sudo apt update
sudo apt install pandoc
```

### 2. Cài đặt LaTeX
```bash
sudo apt install texlive-full
```

### 3. Cài đặt fonts tiếng Việt
```bash
sudo apt install fonts-noto fonts-dejavu fonts-liberation
```

## Sử dụng

### Tạo báo cáo PDF
```bash
make
```

### Xóa file output
```bash
make clean
```

### Các bước thực hiện

1. Tạo file `.md` trong thư mục `content/`, tên file đặt theo cấu trúc `<STT>_<tên file>.md`.
2. Viết nội dung bằng Markdown
3. Chạy `make` để tạo PDF

## Cấu trúc thư mục

```
personal-report/
├── content/
│   ├── *.md                    # Nội dung báo cáo (Markdown)
│   └── metadata.yaml           # Thông tin metadata
├── title/
│   ├── default_template.tex    # Template LaTeX
│   └── logo.png               # Logo trường/khoa
├── release/
│   └── report.pdf             # File PDF đầu ra
├── makefile                   # Build script
└── README.md                  # Hướng dẫn này
```

## Cấu hình metadata.yaml

```yaml
title: "Tiêu đề báo cáo"
subtitle: "Phụ đề"
author:
  - name: "Họ và tên"
    id: "MSSV"
    email: "email@example.com"
supervisor:
  - title: "TS."
    name: "Tên giảng viên"
institute: "TÊN TRƯỜNG"
faculty: "TÊN KHOA"
course: "KHÓA HỌC"
subject: "TÊN MÔN HỌC"
logo: "title/logo.png"
langvi: true
numbersections: true
toc: true
```

## Khắc phục lỗi

### Lỗi font tiếng Việt
```bash
sudo apt install fonts-noto-cjk
fc-cache -fv
```

### Lỗi thiếu package LaTeX
```bash
sudo apt install texlive-latex-extra texlive-fonts-extra
```
