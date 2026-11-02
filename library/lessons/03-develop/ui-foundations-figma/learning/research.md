# UI Foundations: Building in Figma — desk research

*Ngày: 2026-10-31. Giai đoạn research: chưa viết lesson, chưa có brief. Mục đích: gom nguồn trong repo, Notion và web cho các learning objectives, đánh dấu nguồn nào chính thức, nguồn nào chỉ là blog.*

## 1. Bối cảnh đã chốt với Winnie

- Buổi 90 phút, trong đó khoảng 10 phút đầu xem file của mentee, còn khoảng 80 phút để dựng.
- Mentee làm ngay từ đầu, trên file của chính họ. Không có phần demo trước.
- Winnie chỉ ra chỗ sai và sửa cùng mentee ngay lúc làm.
- Giữ grid, 8pt, typography, color ở buổi này nhưng ngắn, chỉ đủ để dựng variables và component. Phần phán đoán visual để buổi UI Fundamentals.
- Không có AI trong buổi này.
- Lesson viết generic, không nhắc tên mentee.

Learning objectives (từ coaching plan):
1. Tổ chức file Figma để ai cũng tìm được đường
2. Dùng auto layout và variables để dựng layout linh hoạt
3. Tạo component và variants từ màn hình của chính mình
4. Điều chỉnh layout qua các breakpoint

## 2. Trong repo và Notion

| Nguồn | Dùng được gì | Lưu ý |
|---|---|---|
| `library/lessons/03-develop/design-system/materials/design-system-lesson.md` (mục "Atomic Design in Figma") | Tokens là Variables, component variants, quy tắc đặt tên `a/m/o`, 8pt grid | Bản nháp; trùng một phần với buổi này, cần chia ranh giới với buổi Design System |
| `library/_recovered-2026-10-02/.../ui-fundamentals-lesson.md` | 5 layer (space, hierarchy, type, colour, component) | Bản khôi phục, README ghi nhầm là đã ở `03-develop/`. Đây là buổi sau, không dạy lại ở đây |
| Notion "Overview & Learner Profile" của mentee | Gap ưu tiên số 1: Figma craft (auto layout, variables, components, file sạch) | Trang riêng của coach, không đưa nội dung cá nhân vào lesson |
| Notion "Day 1: Learn Figma" (2019), "UI/UX Class" (2023) | Ghi chú cũ của Winnie | Chưa đọc kỹ, cần mở nếu muốn tái dùng |

## 3. Nguồn ngoài

Nguồn chính thức dùng được để nêu như sự thật. Blog chỉ dùng làm gợi ý và phải nói rõ là ý kiến.

### Chính thức

| Chủ đề | Nguồn | Điều nguồn nói |
|---|---|---|
| Variables, collections, modes, alias | [Create and manage variables and collections](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables-and-collections), [Modes for variables](https://help.figma.com/hc/en-us/articles/15343816063383-Modes-for-variables) (Figma Help) | Tạo collection, tạo variable, alias bằng "Create alias", mỗi collection có mode riêng, số mode phụ thuộc gói |
| Auto layout, Hug / Fill / Fixed, min và max | [Figma Help: Guide to auto layout](https://help.figma.com/hc/articles/360040451373) | Hug theo nội dung con; Fill chỉ áp cho con của auto layout; gõ số vào width sẽ chuyển sang Fixed; min và max dùng được cùng các chế độ khác |
| Component properties | [Explore component properties](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties), [Create and manage component properties](https://help.figma.com/hc/en-us/articles/8883756012823-Create-and-manage-component-properties) (Figma Help) | Bốn loại: boolean, instance swap, text, variant. Boolean chỉ điều khiển ẩn hiện layer. Variant property chỉ tạo từ component set cha |
| Breakpoint | [Material Design 3: Breakpoints](https://m3.material.io/foundations/layout/applying-layout), [Android Developers: window size classes](https://developer.android.com/develop/ui/views/layout/use-window-size-classes) | Compact dưới 600dp, medium 600 đến 839dp, expanded 840 đến 1199dp, large 1200 đến 1599dp, extra-large từ 1600dp. Compact và medium nên một pane, expanded và large nên hai pane |
| Contrast màu | [WCAG 2.2 Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) (W3C) | 4.5:1 cho chữ thường, 3:1 cho chữ lớn (từ 18pt, hoặc 14pt đậm); so sánh không làm tròn nên 4.499:1 là trượt |
| Design tokens | [Design Tokens Format Module 2025.10](https://tr.designtokens.org/format/) (Design Tokens Community Group) | Bản ổn định đầu tiên, 2025-10-28. Mỗi token có type và value theo type đó. Mới đọc qua đoạn trích, chưa đọc toàn văn |

### Blog và ý kiến (dùng thận trọng)

| Chủ đề | Nguồn | Điều nguồn nói |
|---|---|---|
| Tách primitive và semantic | [Red Hat UX: Figma variables and styles](https://ux.redhat.com/get-started/designers/figma-variables-and-styles), [Using design tokens as variables](https://designtokens.substack.com/p/using-design-tokens-as-variables) | Component dùng semantic, không dùng primitive trực tiếp. Red Hat nói chặt hơn các nguồn khác: không dùng primitive trừ khi bắt buộc. Đây là lựa chọn của từng team |
| Tên variable dạng đường dẫn | cùng hai nguồn trên | Ví dụ `typography/heading/h1/font-size` |
| Tổ chức file | [designproject.io](https://designproject.io/blog/how-to-organize-figma-files/), [Design Shack](https://designshack.net/articles/business-articles/figma-team-collaboration) | Một quy ước đặt tên nhất quán; tách page nháp, page duyệt, page handoff; dùng section; một page ghi chú quy tắc. Không phải chuẩn |
| 8pt grid | [ls.graphics](https://www.ls.graphics/blog/why-8pt-grid-the-math-behind-clean-ui), [Queensland Government Design System: spacing](https://www.designsystem.qld.gov.au/styles/spacing/design) | Thang 4, 8, 16, 24, 32, 48, 64, 96; số nguyên ở 1x, 2x, 3x. Nhiều nguồn khuyên lai: 4pt cho chi tiết nhỏ, 8pt cho phần còn lại. Cỡ chữ theo thang riêng, không theo 8pt. Chưa đối chiếu tài liệu gốc của Material hay Carbon |

## 4. Chỗ chưa chắc

- Bài viết cộng đồng nói alias giữa collection chỉ lấy giá trị, không chọn được mode. Bài đã cũ (khoảng 3 năm) và chưa có nguồn mới xác nhận. **Phải thử trong Figma trước khi dạy.**
- Một tutorial bên thứ ba nói Fixed width bỏ qua min và max. Tài liệu chính thức của Figma không nói vậy. Không dùng.
- Số mode tối đa phụ thuộc gói Figma của mentee; cần hỏi trước buổi học.
- Chưa tìm nguồn có số liệu về tỷ lệ designer dùng hay không dùng auto layout hoặc variables. Không nêu con số nào trong lesson trừ khi có nguồn.
- Phương pháp "nền tảng ngắn rồi dựng variables" là cách dạy của Winnie, không có nghiên cứu nào đi kèm.

## 5. Còn mở (cần Winnie quyết trước brief)

1. Với 80 phút, bỏ hoặc chuyển thành homework nhiệm vụ nào trong năm nhiệm vụ: dọn file, variables, auto layout, component và variants, breakpoints.
2. Ranh giới với buổi Design System: buổi này dừng ở variables cộng một vài component, hay đi đến cả quy tắc đặt tên `a/m/o`?
3. Guide gửi trước buổi (dọn file) có nằm trong phạm vi lesson này không.
