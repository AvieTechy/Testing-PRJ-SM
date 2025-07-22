# Personal Report Template

## Cài đặt

Đảm bảo máy của bạn đã cài đặt `pandoc` và `LaTeX`.

### 1. Cài đặt Pandoc

**macOS (sử dụng Homebrew):**
```bash
brew install pandoc
```

**Ubuntu:**
```bash
sudo apt update
sudo apt install pandoc
```

### 2. Cài đặt LaTeX

**macOS:**
Cài đặt MacTeX, bao gồm `pdflatex` và các gói hỗ trợ tiếng Việt.
Truy cập [MacTeX](https://www.tug.org/mactex/) để tải về và cài đặt.

**Ubuntu:**
```bash
sudo apt update
sudo apt install texlive-full
```
Gói `texlive-full` thường bao gồm hỗ trợ tiếng Việt. Nếu gặp lỗi font, bạn có thể cần cài đặt thêm `texlive-lang-vietnamese`.


## 3. Cài đặt gói babel-vietnamese
**macOS (sử dụng MacTeX):**
```bash
sudo tlmgr update --self
sudo tlmgr install babel-vietnamese
```

**Ubuntu (sử dụng TeX Live):**
```bash
sudo tlmgr update --self
sudo tlmgr install babel-vietnamese
```
Nếu `tlmgr` không được tìm thấy, đảm bảo rằng TeX Live đã được cài đặt đúng cách và đường dẫn đến các tệp thực thi của TeX Live đã được thêm vào `PATH` của hệ thống.

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
