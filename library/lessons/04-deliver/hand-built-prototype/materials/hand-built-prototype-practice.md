---
title: "Hand-Built Prototype: Practice"
type: practice
program: standalone
lesson: hand-built-prototype
duration: "khoảng 2 giờ, làm ở nhà"
draft: true
---

## Goal

Bạn dựng một flow bấm được trong Figma cho một task, từ starting point đến màn cuối, có ít nhất một overlay và một component có variant. Sau đó bạn đưa flow cho một người khác thử và ghi lại họ đã khựng ở đâu. Đầu ra là đầu vào để bạn test thật ở buổi sau.

## Before you start

- Một task đã chọn, có ít nhất ba bước. Nếu chưa có, dùng task "đặt lịch hẹn" trong Practice Dataset của bài học.
- Flow hoặc sơ đồ các bước của task, vẽ trên giấy hoặc bất kỳ công cụ nào.
- Một bạn học để test, hoặc một người bạn sẵn sàng ngồi thử.
- Component từ bài Design System. Nếu chưa có, tự dựng một component có hai state.

## Steps

### Step 1 · Vẽ flow · 20 phút · YOU

- Liệt kê từng bước người dùng làm, theo thứ tự họ làm, không theo thứ tự màn hình.
- Đánh dấu các chỗ có thể sai: nhập sai, chọn giờ đã kín, bấm nhầm.
- Viết một câu hỏi test duy nhất: bạn muốn biết điều gì khi người dùng đi qua flow này?

### Step 2 · Dựng và nối các màn · 60 phút · YOU

- Dựng ba đến năm màn ở mức low fidelity. Dùng khung và thanh xám, chưa cần chữ thật.
- Đặt starting point trên màn đầu tiên và đặt tên cho nó.
- Nối các màn theo flow. Với mỗi kết nối, ghi lại trigger, action và transition, và tự hỏi vì sao bạn chọn từng thứ.
- Thêm một overlay cho một hành động cần giữ người dùng ở màn hiện tại (ví dụ: hộp xác nhận).
- Thêm một đường lỗi và một trạng thái trống.

### Step 3 · Dựng component và Smart Animate · 20 phút · YOU

- Tạo một component có ít nhất hai variant (ví dụ: Default và Pressed, hoặc chọn và không chọn).
- Nối các variant bằng interactive component. Chỉ nối các variant trong cùng một component set.
- Nếu có chuyển động Smart Animate, nhân bản frame và kiểm tra viền tím trong tab Prototype. Layer nào không có viền thì tên hoặc vị trí trong hierarchy đã khác.

### Step 4 · Tự kiểm tra và test · 40 phút · YOU

- Tự bấm qua toàn bộ flow từ starting point. Ghi lại mọi dead end.
- Sửa các dead end và thiếu state trước khi đưa cho người khác.
- Đưa prototype cho một người thử làm task. Chỉ quan sát và ghi lại chỗ họ dừng hoặc hỏi. Không giải thích.
- Sau khi họ làm xong, hỏi một câu mở: bạn kỳ vọng điều gì xảy ra ở chỗ bạn dừng lại?

### Step 5 · Viết ghi chú test · 10 phút · YOU

- Với mỗi chỗ người test khựng, ghi là lỗi thiết kế, lỗi prototype, hay chưa đủ thông tin để kết luận.

## Output

- Link Figma của flow, với starting point đã đặt tên.
- Một trang trong file ghi câu hỏi test và flow bạn muốn kiểm tra.
- Một trang ghi chú test: chỗ người test dừng, câu họ trả lời, và phân loại lỗi.

## Self-check

- [ ] Flow có starting point, và đi từ đầu đến cuối không có dead end.
- [ ] Có ít nhất một overlay, và có lý do cho việc dùng overlay thay vì màn mới.
- [ ] Có ít nhất một đường lỗi hoặc trạng thái trống.
- [ ] Component có ít nhất hai variant, nối bằng interactive component.
- [ ] Layer trong các frame chuyển động có cùng tên và cùng vị trí trong hierarchy.
- [ ] Câu hỏi test được viết trước khi test, không viết sau.
- [ ] Ghi chú test phân loại được từng lỗi là lỗi thiết kế hay lỗi prototype.

## If you get stuck

- **Smart Animate không chuyển động.** Mở tab Prototype và xem layer nào có viền tím. Layer không có viền là layer có tên hoặc vị trí khác. Nhân bản frame thay vì dựng lại.
- **Không biết dùng overlay hay màn mới.** Nếu người dùng không rời khỏi màn hiện tại, dùng overlay.
- **Không có bạn để test.** Nhờ một người khác trong nhóm. Nếu không có ai, tự làm nhưng ghi rõ trong ghi chú là bạn tự test và kết quả có thể thiên lệch.
- **Prototype bị lag.** Giảm số ảnh và bỏ bớt transition phức tạp. Thử mở ở cửa sổ ẩn danh.
