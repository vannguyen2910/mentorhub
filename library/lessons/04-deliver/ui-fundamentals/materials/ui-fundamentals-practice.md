---
title: "UI Fundamentals: Practice"
type: practice
program: standalone
lesson: ui-fundamentals
duration: "16 min in class + homework"
draft: true
---

## Goal

Bạn chọn một trong các concept của chính mình cho một bước trong process map, và nói được vì sao bằng một lý do không có chữ "trông". Sau buổi này bạn có một decision sheet ghi lý do từng quyết định và một token set rút ra từ concept đã chọn. Cả hai là đầu vào cho buổi dựng trong Figma.

## Before you start

Phần này làm trước buổi học.

- Sitemap và process map từ bài Information Architecture Basics.
- Giấy và bút, hoặc một công cụ vẽ bất kỳ. Concept chỉ cần là thanh xám và hình đơn giản, chưa cần chữ thật.
- Một component từ thư viện công khai mà bạn thấy khó hiểu (ví dụ GOV.UK Design System, Material, Carbon). Đừng tìm hiểu lý do trước, vì sự khó hiểu chính là nguyên liệu của Layer 5.
- Cheat sheet 5 layer: `assets/cheat-sheets/ui-fundamentals-cheat-sheet.svg`.

### Pre-class 1 · Chọn flow và bước then chốt · 15 phút · YOU

- Đọc lại process map và chọn main flow.
- Chọn một bước then chốt, nơi người dùng phải hành động hoặc ra quyết định.
- Viết một câu về việc người dùng cần làm ở bước đó. Câu này là "job" mà Layer 2 dùng để kiểm tra hierarchy.

### Pre-class 2 · Vẽ 2 đến 3 concept · 30 phút · YOU

- Mỗi concept là một màn hình cho bước vừa chọn.
- Các concept khác nhau về cấu trúc, không chỉ khác màu hay font.
- Dùng thanh xám cho chữ và hình đơn giản cho nút, không viết nội dung thật.
- Dừng ở mức thô. Concept càng bóng bẩy thì bạn càng dễ bảo vệ nó bằng gu.

## Steps

Phần này làm trong buổi học, 16 phút.

### Step 1 · Chọn theo cảm giác · 2 phút · YOU

- Chọn concept bạn sẽ đưa vào sản phẩm và nói lý do trong một câu.
- Winnie ghi lại câu này để so sánh ở cuối buổi.

### Step 2 · Chạy 5 layer · 8 phút · YOU

- Chạy lần lượt Space, Hierarchy, Type, Colour, Component lên từng concept.
- Dừng ở layer đầu tiên không ổn của mỗi concept.
- Với mỗi quyết định, điền một dòng vào decision sheet (mẫu bên dưới).
- Layer 1 và 2 đối chiếu với process map: gì thuộc cùng nhóm ở bước này, và hành động chính duy nhất là gì.
- Thử blur và desaturate lên concept của bạn. Mỗi thử nghiệm chỉ mất vài giây.

### Step 3 · Chọn một concept · 1 phút · YOU

- Chọn một concept.
- Với mỗi concept còn lại, viết một dòng giải thích vì sao thua, theo layer chứ không theo gu.

### Step 4 · Giải thích với developer · 5 phút · YOU

- Winnie đóng vai developer và hỏi "says who?" cho từng dòng của decision sheet.
- Bạn trả lời cho đến khi lý do đứng được mà không cần chữ "trông".
- Cuối bước, so câu ở Step 1 với lý do bây giờ: lý do có thay đổi không?

## Homework

### Step 5 · Hoàn thiện decision sheet · 20 phút · YOU

- Mỗi trong năm layer có một dòng với lý do chịu được câu hỏi "says who?".
- **File:** `decision-sheet.md`

### Step 6 · Tinh chỉnh concept đã chọn · 40 phút · YOU

- Làm thành một màn hình sạch, chỉ ở trạng thái default.
- Sửa layer đầu tiên không ổn, và chỉ sửa đúng chỗ đó.
- Không thêm màn hình thứ hai và không thêm state khác.
- **File:** `chosen-concept.png`

### Step 7 · Viết token set · 30 phút · YOU

- Liệt kê spacing, cỡ chữ và role màu mà concept thật sự dùng.
- Mọi giá trị spacing nằm trên thang 8. Chữ dùng tối đa ba cỡ và hai weight. Mỗi màu có một role.
- Ghi ít nhất một thứ vẫn chưa được định nghĩa.
- Dùng `assets/layer-4-colour/token-audit-template.svg` làm bố cục.
- **File:** `token-set.md`

### Step 8 · Chạy 5 layer lên một component · 20 phút · YOU

- Dùng component bạn mang từ thư viện công khai.
- Ghi layer nào không resolve, rồi viết một câu hỏi bạn sẽ hỏi team về nó. Câu hỏi để hỏi, không để kết tội: "Mình chạy component này qua năm check và layer X chưa resolve với mình. Anh chị giải thích giúp mình lý do được không?"
- **File:** `component-question.md`

### Step 9 · Nhờ AI đánh giá, rồi kiểm tra · 20 phút · AI soạn nháp, bạn kiểm tra · tuỳ chọn

- **AI soạn nháp:** đánh giá concept theo năm layer, theo đúng thứ tự, với mỗi layer nêu quyết định đã đưa ra, nó có đứng vững không và câu nói với developer.
- **Bạn kiểm tra:** lấy một nhận định về contrast mà AI đưa ra và đo lại bằng một contrast checker. Ghi AI đúng hay sai.
- AI thường khẳng định một cặp màu đạt AA khi thực tế không đạt, với cùng giọng chắc chắn như mọi câu khác. Phần nào đo được thì đo, phần nào không đo được thì tin chậm hơn giọng của công cụ.
- **File:** `ai-check.md`

## Decision sheet

Mỗi dòng ghi một quyết định.

| Layer | Quyết định (concept chọn) | Luật hoặc nguyên tắc | Câu nói với developer | Vì sao concept khác thua |
|---|---|---|---|---|
| 1 · Space | | | | |
| 2 · Hierarchy | | | | |
| 3 · Type | | | | |
| 4 · Colour | | | | |
| 5 · Component | | | | |

## Output

- `decision-sheet.md`
- `chosen-concept.png`
- `token-set.md`
- `component-question.md`
- `ai-check.md` (tuỳ chọn)

## Self-check

- [ ] Decision sheet có đủ năm dòng, và mỗi dòng có một lý do không dùng chữ "trông".
- [ ] Mỗi concept còn lại có một dòng vì sao thua, theo layer.
- [ ] Mọi giá trị spacing trong token set nằm trên thang 8.
- [ ] Token set ghi ít nhất một thứ chưa được định nghĩa.
- [ ] Concept đã chọn qua được bài thử blur: có một thứ vẫn nổi lên khi bị làm mờ.
- [ ] Câu hỏi về component ở dạng hỏi, không phải kết luận.

## If you get stuck

- **Chưa có concept nào khác biệt về cấu trúc:** thử đổi vị trí của hành động chính (đầu trang, cuối trang, cố định ở đáy) hoặc cách nhóm nội dung (một danh sách dài hay hai nhóm). Hai cách đó khác nhau về cấu trúc.
- **Không tìm ra layer nào không ổn:** chạy blur rồi desaturate lên concept. Nếu vẫn không thấy gì, ghi rõ "layer này đạt" cùng lý do. Decision sheet vẫn cần một dòng cho layer đó.
- **Không biết bước nào là bước then chốt:** chọn bước mà nếu người dùng làm sai thì họ mất công hoặc mất tiền.
