---
title: "UI Foundations: Building in Figma"
type: lesson
audience: private-training
level: beginner
duration: "90 min"
---

## Purpose
Sau buổi này, học viên dựng được một component set chạy ở ít nhất hai kích thước màn hình, từ chính màn hình của mình, bằng auto layout và variables, trong một file đã được tổ chức rõ ràng.

## Structure
1. Mở đầu, 10 phút: xem file học viên đã dọn theo guide gửi trước buổi (pages, tên layer, cấu trúc) và chốt màn hình sẽ làm việc.
2. Nhiệm vụ 1, Variables, 22 phút: học viên chọn thang spacing 8pt, type scale và bộ màu nhỏ từ màn hình của mình, rồi tạo collection, đặt tên theo đường dẫn, dùng alias giữa primitive và semantic.
3. Nhiệm vụ 2, Auto layout, 18 phút: dựng lại một màn hình bằng auto layout, dùng Hug, Fill, Fixed, min và max, gắn padding và gap vào variables.
4. Nhiệm vụ 3, Component và variants, 20 phút: biến hai đến ba phần tử lặp lại (ví dụ nút, thẻ, thanh điều hướng) thành component, thêm variant property và component property.
5. Nhiệm vụ 4, Breakpoints, 14 phút: điều chỉnh màn hình và component cho một breakpoint thứ hai, kiểm tra component co giãn đúng.
6. Kết, 6 phút (gồm 3 phút dự phòng): rà success check, ghi lại việc còn dở thành homework.

Tổng 90 phút. Nếu buổi chạy quá giờ, Nhiệm vụ 4 rút còn một component và một màn hình.

Cách dạy: học viên làm ngay từ đầu trên file của mình, không có phần demo trước. Winnie chỉ ra chỗ sai và sửa cùng học viên ngay lúc làm.

## Learning objectives
1. Kiểm tra được file của mình theo guide: pages, tên layer và cấu trúc đủ rõ để người khác tìm đường (kiểm ở phần mở đầu, việc dọn file làm trước buổi).
2. Dựng được layout linh hoạt bằng auto layout, với spacing, màu và cỡ chữ lấy từ variables.
3. Tạo được component và variants từ màn hình của mình, dùng đúng loại property (variant, boolean, text, instance swap).
4. Điều chỉnh được layout và component cho ít nhất hai kích thước màn hình.

Success check: file có pages, tên layer và cấu trúc rõ; một component set chạy được ở ít nhất hai kích thước màn hình.

## Key decisions
- Ví dụ chạy: sitemap và màn hình của chính học viên, không dùng case mẫu.
- AI: không có trong buổi này (theo coaching plan, đây là buổi thuần kỹ thuật).
- Cắt: nhiệm vụ dọn file không làm trong buổi, chuyển thành guide gửi trước và 10 phút kiểm ở đầu buổi. Objective "tổ chức file" vẫn được kiểm bằng success check.
- Nền tảng (grid, 8pt, typography, color) giữ ngắn, chỉ đủ để dựng variables, nằm trong Nhiệm vụ 1. Học viên chọn giá trị từ file của mình rồi mới đặt tên.
- Hoãn sang buổi UI Fundamentals: phán đoán visual (5 layer) và lý do chọn từng giá trị.
- Hoãn sang buổi Design System: quy tắc đặt tên đầy đủ theo atomic (`a/m/o`), tài liệu hoá hệ thống, nhiều hơn một vài component.
- Lesson viết generic, không nhắc tên học viên hay chi tiết nhận dạng.
- Nguồn gốc ý tưởng: coaching plan của một học viên private, ghi `source: adapted-from-private-session` khi viết front matter của lesson.
- Câu hỏi mở cho Winnie:
  1. Guide gửi trước buổi (dọn file) có nằm trong phạm vi lesson này không, hay làm riêng như một tài liệu.
  2. Ranh giới với buổi Design System: dừng ở variables cộng một vài component, hay thêm quy tắc đặt tên `a/m/o`.
  3. Có chọn thêm một ví dụ lỗi thường gặp cho mỗi nhiệm vụ không (spacing lẻ, màu gõ tay, layer "Frame 123", component không co giãn).

## Sources
Chi tiết ở `learning/research.md`. Nguồn chính thức dùng được để nêu như sự thật:
- Figma Help: variables và collections, modes, auto layout, component properties.
- Material Design 3, Breakpoints: compact dưới 600dp, medium 600 đến 839dp, expanded 840 đến 1199dp.
- W3C WCAG 2.2, Understanding 1.4.3: 4.5:1 cho chữ thường, 3:1 cho chữ lớn.
- Design Tokens Community Group, Format Module 2025.10.

Nguồn blog chỉ làm gợi ý: tách primitive và semantic, thang 8pt, cách tổ chức file.

## [to confirm]
- Alias giữa collection có chọn được mode không (nguồn cộng đồng cũ nói không); thử trong Figma trước khi dạy.
- Gói Figma của học viên cho phép bao nhiêu mode.
- Chưa có nguồn cho tỷ lệ designer dùng auto layout hay variables; không nêu con số nào.
- "Nền tảng ngắn rồi dựng variables" là phương pháp của Winnie, không có nghiên cứu đi kèm.
