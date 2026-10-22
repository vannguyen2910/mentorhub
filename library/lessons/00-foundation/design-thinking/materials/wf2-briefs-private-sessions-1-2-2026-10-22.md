---
title: "WF-2 content briefs from two early private-training sessions"
type: brief-set
source: adapted-from-private-session
status: đã duyệt cả ba brief (2026-10-22), đã áp dụng vào lesson và slide outline. Deck chưa cập nhật
date: 2026-10-22
---

> Ba ý tưởng lấy từ transcript hai buổi đầu của một chương trình private training, đã bỏ tên người, công ty và chi tiết dự án (WF-2). Tài liệu này chỉ đề xuất nơi đặt và soạn brief ngắn. Chưa sửa lesson, slide outline hay deck.

## Đã kiểm tra và không đưa vào

| Ý trong buổi | Lý do |
|---|---|
| Quy tắc một dự án một folder, folder theo stage, output bước trước là input bước sau | Đã có trong `ai-workflow-for-ux-designers-lesson.md` (mục project folder và các learning objective về case folder) |
| Mô tả vấn đề trước, không nêu cách sửa; gắn finding với principle và bằng chứng | Đã có trong `evaluate-current-experience-lesson.md` (phần "Is it a problem, not a fix?", facilitator watch-fors và schema) |
| Thông báo lỗi phải nói sai ở đâu và sửa thế nào | Đã có ở principle 9 trong cùng lesson |
| Làm tay trước, dùng AI sau, rồi so sánh hai bản | Đã là nguyên tắc của lesson (Block 6 trước Block 7) |
| Demo template trên GitHub quá nhanh với người chưa quen Markdown | Là phản hồi về cách dạy, không phải nội dung lesson. Việc cần làm là hướng dẫn từng bước đã hứa với mentee, nằm ở recap của mentee |
| Vị trí công việc của mentee, màn hình dự án cụ thể, lịch học | `[keep private]` |

---

## Nơi đặt đề xuất

| # | Ý tưởng | Đề xuất | Loại thay đổi | Phương án khác |
|---|---|---|---|---|
| 1 | Dùng severity để quyết định khi nào giữ ý kiến, khi nào nhượng bộ, khi nào tìm giải pháp thay thế, lúc người làm sản phẩm từ chối một thay đổi | `library/lessons/01-discover/evaluate-current-experience/materials/evaluate-current-experience-lesson.md` (Block 5 Severity) và slide outline | Cập nhật nhỏ | Câu hỏi thảo luận trong Homework, không đổi thời lượng |
| 2 | Chạy delivery và UX strategy song song trong team có chu kỳ giao hàng ngắn, và cách đề xuất với manager | `library/lessons/00-foundation/design-thinking/materials/design-thinking-lesson.md` (Act 4, sau "A brief is not a problem definition") và slide outline | Cập nhật nhỏ | Block ngắn trong `design-process-with-ai` khi đến lượt sửa lesson đó |
| 3 | Proof of concept khác prototype ở đâu, kèm một ví dụ | Cùng file `design-thinking-lesson.md` (mục Prototype, hiện chỉ có một dòng định nghĩa) và slide outline | Cập nhật nhỏ | Không có |

Cả hai lesson đều đã có deck build sẵn (`slides/`), nên mỗi thay đổi cần đối chiếu lại deck sau khi duyệt.

---

## Brief 1: Evaluate Current Experience (delta) — severity quyết định bước tiếp theo

```yaml
title: "Evaluate Current Experience: severity as a decision rule (delta)"
type: lesson
audience: private-training
level: beginner
duration: "2 phút, lấy từ buffer 8 phút của Block 5 hoặc Block 8"
```

**Purpose.** Sau Block 5, học viên dùng severity để quyết định mình giữ ý kiến, nhượng bộ hay tìm giải pháp thay thế khi người làm sản phẩm không muốn thay đổi, thay vì chỉ nói "nên sửa".

**Lesson hiện có đã bao gồm:** thang 0 đến 4, ba câu hỏi để chấm severity, ma trận 2x2, và quy tắc mô tả vấn đề chứ không mô tả cách sửa. Chưa có phần nối severity với cách làm việc cùng người ra quyết định.

**Structure (chỉ phần thay đổi):**
1. Một tình huống ngắn, không tên: người làm sản phẩm không muốn thêm một pop-up mà designer đề xuất.
2. Ba bước phân tích: nếu không có thay đổi này thì user có bị chặn hoặc mất dữ liệu không; nói bằng principle, bằng chứng và severity chứ không bằng gu hay nhờ vả; nếu thật sự không làm được thì đề xuất cách khác giữ được kết quả cho user (ví dụ thông báo ngay tại chỗ thay cho pop-up).
3. Quy tắc nối: severity 1 đến 2 có thể nhượng bộ hoặc đưa vào backlog; severity 3 cần tranh luận bằng bằng chứng; severity 4 phải giữ trước khi release.

**Key decisions.**
- Đây là cách làm của Winnie, không có nghiên cứu hỗ trợ. Thang severity 0 đến 4 vẫn lấy từ nguồn đã trích trong lesson.
- Học viên có thể không có quyền quyết định. Mục tiêu là đưa bằng chứng rõ cho người quyết định, không phải thắng cuộc tranh luận. Không dạy như thể học viên là người chốt.
- Không dùng ví dụ của công ty hay đồng nghiệp thật.
- Sync: sửa lesson thì sửa slide outline cùng lượt. Số slide và timing dự kiến `[to confirm]` khi viết.

**Open questions for Winnie.**
1. Đưa vào Block 5 như một slide, hay chỉ là câu hỏi thảo luận ở Homework?
2. Có cần một dòng nói rõ người học ở vị trí junior nên báo lên (escalate) thay vì tự quyết?

---

## Brief 2: Design Thinking (delta) — giữ thời gian cho discovery trong team giao hàng nhanh

```yaml
title: "Design Thinking: protecting discovery time in a delivery-driven team (delta)"
type: lesson
audience: private-training
level: beginner
duration: "2 phút, lấy từ Act 4 (10 phút). Lesson hiện kín 90 phút nên cần rút một ý khác"
```

**Purpose.** Học viên nêu được một cách giữ một phần thời gian cho discovery khi team giao hàng theo chu kỳ ngắn, và cách đề xuất việc đó với manager.

**Lesson hiện có đã bao gồm:** "A brief is not a problem definition" và lý do các team bỏ qua Empathise và Define vì quy trình không tạo chỗ cho chúng. Câu cuối của mục nói lesson tạo từ vựng và công cụ để học viên xin lại chỗ đó, nhưng chưa nêu cách làm cụ thể.

**Structure (chỉ phần thay đổi):**
1. Chạy hai việc song song: vẫn giao hàng cho từng sprint, đồng thời dành một phần thời gian cố định cho một cải tiến end-to-end lớn hơn.
2. Phần thời gian đó nhỏ và rõ ràng. Winnie dùng khoảng 30% làm ví dụ (`[to confirm]` đây là quy tắc kinh nghiệm của riêng Winnie, không phải chuẩn).
3. Cách đề xuất: nói "mình vẫn giao hàng, và muốn dành một phần nhỏ thời gian cho hướng lớn hơn", không nói "mình muốn đổi tỷ lệ công việc".
4. Sản phẩm của phần thời gian đó: một flow end-to-end mà các màn hình giao theo sprint nằm bên trong.

**Key decisions.**
- Không nêu con số 30% như một quy tắc. Chỉ dùng như ví dụ và ghi rõ nguồn là kinh nghiệm của người dạy.
- Không nhắc ngân hàng hay công ty cụ thể. Dùng "team có chu kỳ giao hàng hai tuần".
- Cần rút bớt một ý khác trong Act 4 hoặc dùng buffer ở Act 8 để không vượt 90 phút. Winnie chọn ý nào được rút.
- Sync: lesson và slide outline cùng lượt, kèm kiểm tra deck đã build.

**Open questions for Winnie.**
1. Rút ý nào ở Act 4 để lấy chỗ?
2. Có muốn nói rõ đây là kinh nghiệm cá nhân trên slide, hay chỉ để trong speaker notes?

---

## Brief 3: Design Thinking (delta) — proof of concept khác prototype ở đâu

```yaml
title: "Design Thinking: proof of concept vs prototype (delta)"
type: lesson
audience: private-training
level: beginner
duration: "1 phút, không đổi thời lượng nếu thay một câu có sẵn"
```

**Purpose.** Học viên phân biệt được proof of concept (kiểm tra một ý tưởng kinh doanh hoặc kỹ thuật mới trên thực tế) với prototype (kiểm tra trải nghiệm với người dùng).

**Lesson hiện có đã bao gồm:** một dòng định nghĩa trong mục Prototype ("Answers one question: does this idea actually work? Keep it rough and fast"). Dòng này chưa nói ai dùng, để làm gì, và khác prototype ở chỗ nào. Mentee trong buổi vẫn chưa rõ sau một lần giải thích bằng lời, nên định nghĩa hiện tại có thể quá ngắn.

**Structure (chỉ phần thay đổi):**
1. Thay dòng định nghĩa bằng hai câu so sánh: prototype phục vụ việc test trải nghiệm với người dùng; proof of concept phục vụ team product và kỹ thuật kiểm tra một ý tưởng kinh doanh hoặc công nghệ mới.
2. Thêm một ví dụ chung: một sản phẩm tài chính mới mà việc build đầy đủ mất sáu tháng đến một năm. Team dựng bản chạy được trên thị trường trước để xem có nhu cầu không, có thể bỏ qua design standard, rồi quyết định dừng hoặc build tiếp.

**Key decisions.**
- Ví dụ giữ ở mức chung, không dùng tên ngân hàng hay sản phẩm thật.
- Phần "có thể bỏ qua design standard" là mô tả của Winnie về thực tế ngành, `[to confirm]` bằng một nguồn nếu muốn đưa lên slide.
- Sync: sửa `design-thinking-lesson.md` thì sửa slide outline cùng lượt.

**Open questions for Winnie.**
1. Có muốn thêm ví dụ này lên slide, hay chỉ để trong speaker notes?

---

## Sources

- Brief 1: `evaluate-current-experience-lesson.md` (thang severity, ba câu hỏi, watch-fors).
- Brief 2: `design-thinking-lesson.md`, mục "The Pattern Most Teams Follow".
- Brief 3: `design-thinking-lesson.md`, mục Prototype.
- Cả ba brief đều là cách làm của Winnie, chưa có nguồn nghiên cứu. Cần tìm nguồn trước khi nêu bất kỳ con số hay khẳng định chung nào trên slide.
- Nguồn gốc: hai buổi private training (đã ẩn danh theo WF-2).
