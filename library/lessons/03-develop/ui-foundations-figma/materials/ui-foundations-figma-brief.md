---
title: "UI Foundations: Building in Figma"
type: lesson
audience: private-training
level: beginner
duration: "90 min"
---

## Purpose
Sau buổi này, học viên dựng được một component set chạy ở ít nhất hai kích thước màn hình, từ concept đã chọn ở buổi UI Fundamentals, bằng variables và auto layout, trong một file đã được tổ chức rõ ràng.

## Structure
Thứ tự: variables, auto layout, component, breakpoints. Mỗi nhiệm vụ mở bằng một lỗi thật trên file mẫu "xấu" (xem Key decisions), rồi học viên làm trên concept của mình.

1. Mở đầu, 10 phút: xem file học viên đã dọn theo guide gửi trước buổi (pages, tên layer, cấu trúc) và chốt concept sẽ dựng. Đầu vào có sẵn từ buổi UI Fundamentals: `chosen-concept.png`, decision sheet và token set.
2. Nhiệm vụ 1, Variables, 15 phút: 4 phút tìm lỗi trên file mẫu (ba sắc cam gần giống nhau, nhiều xám gần giống nhau, tất cả gõ tay) và thay một nhóm bằng variable. Sau đó, 11 phút học viên đưa token set của mình vào file: hai collection (primitive và semantic), ba nhóm (spacing, vai trò màu, cỡ chữ), đặt tên theo vai trò, alias từ semantic về primitive. Chưa dạy modes.
3. Nhiệm vụ 2, Auto layout, 21 phút: 5 phút sửa trên file mẫu (hàng cha Hug và con Fill bị cắt chữ, group dùng làm bố cục, kích thước Fixed khắp nơi). Sau đó, 16 phút học viên dựng màn hình concept của mình bằng auto layout với Hug, Fill, Fixed, min và max, gắn padding và gap vào variables.
4. Nhiệm vụ 3, Component và variants, 24 phút: biến hai đến ba phần tử lặp lại (ví dụ nút, thẻ, thanh điều hướng) thành component, thêm variant property và component property. Lỗi để chỉ ra: nút copy (Button, Button 2, Button final), detach instance, định nghĩa property sau khi đã tạo variant, tên variant Yes và No.
5. Nhiệm vụ 4, Breakpoints và modes, 14 phút: thêm một collection có mode (Compact, Medium, Expanded), điều chỉnh màn hình và component cho một breakpoint thứ hai, kiểm tra component co giãn đúng. Đây là phần chính, không cắt.
6. Kết, 6 phút (gồm 3 phút dự phòng): rà success check, ghi lại việc còn dở thành homework.

Tổng 90 phút, buffer 3 phút trong phần Kết. Nếu buổi chạy quá giờ, Nhiệm vụ 3 rút còn hai component.

Cách dạy: học viên làm ngay từ đầu, không có phần demo trước. Winnie chỉ ra chỗ sai và sửa cùng học viên ngay lúc làm. Mỗi nhiệm vụ có sáu sơ đồ khái niệm hỗ trợ (đã vẽ, xem Sources).

## Learning objectives
1. Kiểm tra được file của mình theo guide: pages, tên layer và cấu trúc đủ rõ để người khác tìm đường (kiểm ở phần mở đầu, việc dọn file làm trước buổi).
2. Tạo được hai collection variables (primitive và semantic) từ token set của mình và gắn vào layer, thay cho màu và số gõ tay.
3. Dựng được layout linh hoạt bằng auto layout, dùng đúng Hug, Fill, Fixed, min và max, với spacing, màu và cỡ chữ lấy từ variables.
4. Tạo được component và variants từ concept của mình, dùng đúng loại property (variant, boolean, text, instance swap).
5. Điều chỉnh được layout và component cho ít nhất hai kích thước màn hình bằng một mode của variables.

Success check: file có pages, tên layer và cấu trúc rõ; màu và spacing trong file lấy từ variables; một component set chạy được ở ít nhất hai kích thước màn hình.

## Key decisions
- Thứ tự: học sau UI Fundamentals. Màn hình để dựng là concept học viên đã chọn ở buổi đó, kèm decision sheet và token set. Học viên chưa có màn hình sau bài Information Architecture, nên concept này là màn hình đầu tiên của họ.
- Ví dụ chạy: concept đã chọn ở UI Fundamentals, không dùng case mẫu.
- AI: không có trong buổi này (theo coaching plan, đây là buổi thuần kỹ thuật). Mục AI in Practice của lesson vẫn bắt buộc theo LP-4, nên cần quyết định cách viết (xem câu hỏi mở 3).
- Variables đứng trước auto layout (chốt 2026-11-24): Nhiệm vụ 2 gắn padding và gap vào variables nên cần variables có trước. Thu còn 15 phút và chưa dạy modes. Modes chuyển sang Nhiệm vụ 4 vì chỉ cần cho breakpoint. Phương án không chọn: auto layout và component trước, variables làm bước refactor sau. Chưa thử với học viên thật.
- Nhiệm vụ 4 là phần chính (chốt 2026-11-24). Giáo trình và JD ít nhắc breakpoint, nhưng Winnie giữ vì nó là chỗ modes có tác dụng thấy được.
- Gói Figma của học viên là Pro (chốt 2026-11-24): có đủ mode (tối đa 10 mỗi collection theo blog Figma 2025-10-28).
- File mẫu "xấu" (chốt dùng 2026-11-24, cách xếp vào buổi là câu hỏi mở 1): đã dựng, có đủ 8 dấu hiệu (tên layer mặc định, hex cứng, detached instance, nút copy thay cho variant, group làm bố cục, cha Hug và con Fill, kích thước Fixed khắp nơi, một page lẫn nháp và bản cuối). File nằm trong Figma của Winnie (xem [to confirm] về quyền chia sẻ).
- Cắt: nhiệm vụ dọn file không làm trong buổi, chuyển thành guide gửi trước và 10 phút kiểm ở đầu buổi. Objective "tổ chức file" vẫn được kiểm bằng success check. Prototype, Dev Mode, handoff, plugin và tính năng AI trong Figma không dạy ở buổi này.
- Nền tảng (grid, 8pt, typography, color) giữ ngắn, chỉ đủ để dựng variables. Học viên đã chọn giá trị ở buổi UI Fundamentals rồi mới đặt tên.
- Đã dạy ở buổi UI Fundamentals: phán đoán visual (5 layer) và lý do chọn từng giá trị. Nhiệm vụ 1 bắt đầu từ token set học viên đã rút ra ở buổi đó, nên không dạy lại thang 8pt và type scale, chỉ chuyển giá trị thành variables.
- Hoãn sang buổi Design System: quy tắc đặt tên đầy đủ theo atomic (`a/m/o`), tài liệu hoá hệ thống, nhiều hơn một vài component.
- Lesson viết generic, không nhắc tên học viên hay chi tiết nhận dạng. Ghi `source: adapted-from-private-session` ở front matter của lesson.
- Đã chốt 2026-11-24 (Winnie duyệt brief):
  1. File mẫu xấu: mỗi nhiệm vụ 1 và 2 mở bằng 4 đến 5 phút sửa lỗi trên file mẫu, rồi làm trên concept của học viên.
  2. Guide dọn file gửi trước buổi nằm trong lesson (mục Pre-Class Preparation), không làm riêng.
  3. AI in Practice: buổi không dùng AI. Lesson giữ mục này dưới dạng ghi chú nêu rõ điều đó, không có prompt (khác quy tắc LP-4, cần Winnie xác nhận).
  4. Programme line: `ui-ux-fundamentals:06b`, nằm giữa UI Fundamentals (06) và Design System (07).
  5. Auto layout: dạy theo bản "updated", Hug, Fill, Fixed, min và max theo tài liệu Figma; chỗ chưa kiểm ghi `[to confirm]` trong lesson.

## Sources
Chi tiết ở `learning/research.md` (mục A đến J). Nguồn chính thức dùng được để nêu như sự thật:
- Figma Help: variables và collections, modes, auto layout (bản "updated" mặc định cho frame mới từ 2026-07), component properties (năm loại, gồm Slot), bảng so sánh gói.
- Figma blog, Schema 2025 (2025-10-28): Professional tối đa 10 mode mỗi collection, Organization 20.
- Material Design 3, Breakpoints (window size classes): Compact dưới 600dp, Medium 600 đến 839dp, Expanded 840 đến 1199dp.
- W3C WCAG 2.2, Understanding 1.4.3: 4.5:1 cho chữ thường, 3:1 cho chữ lớn.
- Design Tokens Community Group, Format Module 2025.10.

Dùng làm gợi ý, nói rõ là mẫu nhỏ hoặc ý kiến: 12 mô tả công việc junior (auto layout 4 trên 12, variables 3 trên 12, component và design system 9 trên 12, breakpoint 0 trên 12; mẫu nhỏ, thiên lệch chọn mẫu, không phải thống kê); 39 lỗi từ forum Figma, help và blog (số nguồn đếm tay); 12 giáo trình so sánh (khung gần nhất là Figma for Developers v2 của Frontend Masters). Nguồn blog chỉ làm gợi ý: tách primitive và semantic, thang 8pt, cách tổ chức file.

Hình ảnh trong lesson: sáu sơ đồ tự vẽ ở `assets/diagrams/` (Hug, Fill, Fixed; min và max; chuỗi alias primitive đến semantic; component set và property; cấu trúc file gọn; breakpoint là mode) và ảnh chụp `assets/bad-file-sample-screen.png` của file mẫu xấu. Chưa có ảnh chụp giao diện Figma (panel Variables, Auto layout settings, dropdown Width, Properties); cần Winnie chụp hoặc thay bằng slide thao tác trực tiếp.

## [to confirm]
- Alias giữa collection có chọn được mode không khi collection primitive có nhiều mode (nguồn cộng đồng cũ nói không); thử trong Figma trước khi dạy. Sơ đồ alias hiện dùng mode ở semantic trỏ về primitive một mode, mẫu này không phụ thuộc câu hỏi trên.
- Hug, Fill, Fixed, min và max có chạy giống nhau ở auto layout bản "updated" và bản cũ trong frame thường không (help chỉ nói rõ cho Figma Sites). Kiểm trong app trước khi dạy.
- Cặp cha Hug và con Fill bị cắt chữ: quan sát qua API, chưa thử bằng thao tác tay.
- Tên chính xác của panel Variables và đường mở trong giao diện hiện tại (không trang help nào ghi rõ).
- Quyền chia sẻ file mẫu xấu: học viên cần quyền xem và nhân bản (Duplicate). File đang nằm ở bản nháp trong team cá nhân của Winnie, gói Starter (tối đa 3 file trong một folder).
- Số mode thực tế trong gói Pro của học viên (blog Figma ghi 10 mỗi collection).
- Chưa có nguồn cho tỷ lệ designer dùng auto layout hay variables; không nêu con số nào trong lesson.
- "Nền tảng ngắn rồi dựng variables" và "làm ngay, không demo" là phương pháp của Winnie, không có nghiên cứu đi kèm.
