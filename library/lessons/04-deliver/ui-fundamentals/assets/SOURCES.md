# Nguồn ảnh của lesson UI Fundamentals

Chỉ dùng nguồn mở. Mỗi ảnh ghi nguồn, giấy phép và slide dự kiến dùng. Ảnh CC BY-SA phải ghi nguồn khi hiển thị trên slide.

| File | Nguồn | Giấy phép | Dùng cho |
|---|---|---|---|
| `laws-of-ux/hicks-law-plotted-data.svg` | Wikimedia Commons, "Hick's law plotted data.svg" | CC BY-SA 4.0 | Slide "Two laws you'll hear quoted wrongly" (Hick) |
| `layer-3-type/typography-line-terms.svg` | Wikimedia Commons, "Typography Line Terms.svg" | Public domain | Layer 3, line height và baseline |
| `layer-4-colour/wcag-contrast-ratio-thresholds.svg` | Wikimedia Commons, "WCAG contrast ratio thresholds.svg" | CC BY-SA 4.0 | Layer 4, "One rule and a tool" |
| `layer-4-colour/wcag-contrast-ratio-4.5.svg` | Wikimedia Commons, "WCAG contrast ratio 4.5.svg" | CC BY-SA 4.0 | Layer 4, ví dụ 4.5:1 |
| `layer-4-colour/wcag-web-safe-contrast-ratio.svg` | Wikimedia Commons, "WCAG web safe contrast ratio.svg" | CC BY-SA 4.0 | Layer 4, tham khảo thêm |
| `layer-5-components/govuk-*-focus.png` (4 file) | GOV.UK Design System, `src/get-started/focus-states/` | Chưa kiểm tra. Repo là MIT cho code, nội dung thường là OGL. Cần xác nhận trước khi đưa lên site | Layer 5, trạng thái focus của component |

## Chưa có (không tìm được nguồn mở phù hợp)

- Layer 1 và 2: Commons không có ảnh UX, đã tự dựng (xem bảng bên dưới).
- Poster Miller và poster Laws of UX: chưa xác nhận giấy phép. Jakob và Tesler đã tự dựng.
- Ảnh Kurosu và Kashimura: không có bản mở.
- Stimulus set, màn hình tracking giao đồ ăn, ảnh bìa: cần dựng riêng, không pull được.
- Cheat sheet cho practice: cần tự làm theo style `style-reference-schematic.png`.

## Ảnh tự dựng (schematic)

Đã chuyển sang line-art theo Design System (nét 2px, không tô màu, chỉ nhấn bằng `--ink` và một màu `--sienna`) ngày 2026-11-18. Sinh bằng `_generate-schematics.py` (chạy `python3 _generate-schematics.py .` trong thư mục này). Màu trong script là hex tạm (accent tím thay cho `--sienna`), cần đổi sang token khi dựng deck. Chưa có font Syne/Inter, nhãn dùng monospace.

| File | Dùng cho |
|---|---|
| `layer-1-space/proximity-24-vs-8.svg` | Compare Proximity (đổi đúng một biến: gap) |
| `layer-1-space/common-region-two-boundaries.svg` | Compare Common region |
| `layer-1-space/8pt-grid-overlay.svg` | Diagram The 8pt scale |
| `layer-2-hierarchy/four-levers.svg` | Diagram Four levers |
| `layer-2-hierarchy/two-firsts-vs-one-first.svg` | Compare Two firsts |
| `layer-2-hierarchy/f-pattern-scan-path.svg` | F-pattern (hình minh hoạ, không phải dữ liệu eye tracking) |
| `layer-2-hierarchy/von-restorff-emphasis-budget.svg` | Von Restorff, ngân sách nhấn mạnh |
| `layer-3-type/type-scale-three-sizes.svg` | Compare Three and two |
| `layer-4-colour/colour-roles.svg` | Diagram Roles, not palettes |
| `layer-4-colour/token-audit-template.svg` | Mẫu token audit cho practice |
| `layer-5-components/button-states-checklist.svg` | 8 trạng thái của component |
| `laws-of-ux/tesler-complexity-moves.svg` | Tesler's Law |
| `laws-of-ux/jakob-familiar-vs-moved.svg` | Jakob's Law |
| `cheat-sheets/ui-fundamentals-cheat-sheet.svg` | Cheat sheet cho mentee khi practice: 5 layer, câu hỏi, câu nói với dev, hai output. Tiếng Việt, thuật ngữ giữ tiếng Anh |

## Màn hình theo dõi đơn hàng (REAL, dựng trong Figma)

Nguồn: file Figma "UI Fundamentals - REAL screens" (trang "Tracking screen"), dựng bằng code, nội dung giả định. Mỗi trạng thái áp dụng cộng dồn một layer. Font Inter, màn hình 390 x 844.

| File | Dùng cho |
|---|---|
| `tracking-screen/tracking-0-original.png` | Bản gốc (mỗi layer đều có lỗi) |
| `tracking-screen/tracking-1-space.png` | Sau Layer 1, chỉ sửa khoảng cách |
| `tracking-screen/tracking-2-hierarchy.png` | Sau Layer 2, status lên đầu, bản đồ thu thành dải, một primary |
| `tracking-screen/tracking-3-type.png` | Sau Layer 3, ba cỡ chữ và hai weight |
| `tracking-screen/tracking-4-colour.png` | Sau Layer 4, role màu và contrast |
| `tracking-screen/tracking-5-component.png` | Sau Layer 5, nút cùng một kiểu |
| `tracking-screen/tracking-blur-after-layer-2.png` | Slide The blur test |
| `tracking-screen/tracking-desaturate-collapses.png` | Slide The desaturate test, hierarchy mất (bản Layer 1) |
| `tracking-screen/tracking-desaturate-survives.png` | Slide The desaturate test, hierarchy còn (bản Layer 5) |
| `*@2x.png` | Bản độ phân giải gấp đôi, mới có cho 4 ảnh (gốc, type, blur, desaturate collapses). Xuất nốt 5 ảnh còn lại từ Figma khi cần |

Chưa có: stimulus set, ảnh bìa, hai mẫu chữ cho slide contrast.

## Ảnh bìa

| File | Nguồn | Giấy phép | Ghi chú |
|---|---|---|---|
| `cover/pexels-4792351-original.jpg` | Pexels, ảnh 4792351 ("Faceless person demonstrating empty screen on smartphone") | Pexels License (dùng miễn phí, được chỉnh sửa, không cần ghi nguồn) | Ảnh gốc, chưa chỉnh |
| `cover/cover-phone-in-hand.jpg` | Ghép từ ảnh trên và `tracking-screen/tracking-0-original@2x.png` | Như trên | Màn hình theo dõi đơn hàng được ghép vào màn hình điện thoại, cắt theo khung bìa. Dùng trên slide bìa của deck |
