# Series Vocabulary

Nguồn duy nhất cho tên gọi của chương trình, tách ra từ `lesson-details.md` ngày 2026-10-30. Lesson, practice và slide outline dùng đúng các tên này; muốn thêm hoặc đổi tên thì sửa ở đây trước, rồi thêm rule vào `consistency.json` nếu tên cũ phải biến mất.

Quy tắc ngôn ngữ đơn giản (2026-10-05). Mỗi ý chỉ dùng **một tên**, trong mọi thứ học viên đọc. Định nghĩa thuật ngữ ở lần dùng đầu tiên. Không thêm thuật ngữ mới mà chưa thêm vào bảng này.

| Nói | Nghĩa là | Không nói |
|---|---|---|
| **case**, **project folder** | Project học viên làm xuyên suốt, và folder chứa nó | case file, project file |
| **working file** | Một file Markdown mà một activity điền vào, từng section một | living file |
| **context pack** | Các file trong `context/`, được dán vào các bước AI trước tiên | constraint layer |
| **hub** (Knowledge Hub ở lần dùng đầu) | Website liên kết chứa mọi output | final report (chỉ dùng cho hub đã hoàn thiện) |
| **output** | File hoặc trang mà một bước tạo ra | artifact, deliverable |
| **gate** và **check** | Gate là checklist ngắn trước khi đi tiếp. Check là một câu hỏi có hoặc không (1a, 3b ...) | không có |
| **stage map**, **activity flow**, **step card** | Ba góc nhìn: cả series, một activity, một bước | Level 1, Level 2, Level 3 |
| **pattern** (Investigate hoặc Generate) | Hình dạng xuất phát của một activity flow | archetype |
| **alignment check**, **alignment table** | Mỗi decision có truy được về một user need và vượt qua các principle không | alignment matrix |
| **opportunity** | Một user need đáng giải, có evidence đi kèm | không có |
| **source of truth** | Nơi duy nhất một dữ kiện được viết ra; mọi bản tóm tắt được dựng từ đó, không sao chép tay | master copy, duplicate |
| **propose first** | AI liệt kê những gì nó sẽ tạo, kèm nguồn, và không ghi gì cho đến khi học viên duyệt | dry run, preview |
| **research plan** | File markdown ghi research goal, người sẽ phỏng vấn, mission và các research question chính | research brief |
| **facilitator page** | Trang HTML nhỏ giúp người phỏng vấn giữ thứ tự câu hỏi, mở nhánh follow-up, ghi chú và canh giờ; dùng lại được cho các round sau | interview dashboard, script page |
| **transcript** | Bản ghi lời nói thành văn bản của một buổi phỏng vấn hoặc test | bản gỡ băng |
| **consent** | Xin phép người tham gia trước buổi phỏng vấn: ghi hình, dùng cho nghiên cứu nội bộ, không chia sẻ ra ngoài | permission slip |
| **ẩn danh** | Thay tên và thông tin nhận dạng bằng mã, bằng find and replace trên máy, **trước** khi dán vào AI tool | nhờ AI ẩn danh sau khi đã dán |
| **participant code** | Mã thay tên người tham gia trong transcript và ghi chú: P1, P2... | alias, tên giả |
| **quote ID** | Mã của một quote, ví dụ `I01-01` là quote 1 của buổi phỏng vấn 01 (người tham gia P1); quote từ review dùng `R01` | quote number |
| **codebook** | Bộ nhãn (code) dùng để gắn tag cho quote | tag list, label set |
| **AI draft**, **verified copy** | Bản AI trả về, không sửa; và bản sao học viên đã kiểm tra và chỉnh | raw output, final |
| **counterexample** | Ví dụ mâu thuẫn với một theme hoặc một giả thuyết. "Đã tìm, không có" cũng được ghi lại | negative case |
| **hard stop** | Check mà gate không được qua bằng lý do: phải thật sự đạt. Gate 1 có ba: 1b, 1c, 1f | blocker, chặn cứng |

Cách nói đơn giản cho cảnh báo và review trong hub:

- **a decision with no user need behind it** (không dùng "orphan")
- **an opportunity with no decision** (không dùng "uncovered")
- **a decision that pulls against a principle** (không dùng "strain")
- **word for word** (không dùng "verbatim")
- **access levels**: full, limited và no access (không dùng "tiers")
- "**if no, go back to step N**" (không dùng "go-back rule")

Khoá `rel: "strains"` trong file dữ liệu của hub được giữ nguyên; học viên không nhìn thấy nó.
