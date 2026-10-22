---
title: "WF-2 content briefs from a private final session"
type: brief-set
source: adapted-from-private-session
status: brief, chờ Winnie duyệt (chưa tạo lesson, outline hay folder nào)
date: 2026-10-17
---

> Ba ý tưởng lấy từ buổi cuối của một chương trình private training, đã bỏ tên người, công ty và chi tiết dự án (WF-2). Tài liệu này chỉ đề xuất nơi đặt và soạn brief ngắn. Chưa viết lesson, slide outline hay deck.

## Nơi đặt đề xuất

| # | Ý tưởng | Đề xuất | Loại thay đổi | Phương án khác |
|---|---|---|---|---|
| 1 | Dùng lại skill hoặc repo bên ngoài một cách an toàn | `library/lessons/03-develop/ai-prototype-development/materials/lesson-5-reuse-what-others-built.md` (và outline) | Cập nhật nhỏ, không phải lesson mới | Không có, vì lesson đã duyệt và build ngày 2026-10-17 |
| 2a | Quy tắc "prompt, không sửa tay", và cách xử lý khi link GitHub Pages mở sai trang | `library/lessons/03-develop/ai-prototype-development/materials/lesson-3-4-stub.md` (Lesson 4, Publish It) và `lesson-4-slide-outline.md` | Cập nhật nhỏ | Để trong guide `library/guides/publish-your-work-git-github-for-non-technical-designers/` |
| 2b | Nhờ AI ghi nhận hành vi người dùng trên prototype đã publish | Một block trong lesson `refine-and-test` (tuần 6 của chương trình AI Design Workflow), tạo mới khi tới lượt | Block mới trong lesson chưa tồn tại | Bài bonus Lesson 6 trong `ai-prototype-development`, hoặc mục mới trong `04-deliver/solution-validation-user-testing` |
| 3 | Ghi âm mọi buổi làm việc rồi nhờ agent đối chiếu transcript với giả thuyết | Guide mới `library/guides/cross-check-sessions-against-hypotheses/`, được `discover-the-problem` và `refine-and-test` dẫn chiếu | Guide mới | Một block trong `refine-and-test` |

Lý do chọn: ý 1 và 2a đã có chỗ trong lesson hiện có nên chỉ cần phần chênh lệch. Ý 2b và 3 chỉ có ý nghĩa khi học viên đã có prototype và giả thuyết, nên thuộc giai đoạn kiểm chứng. Thư mục lesson của chương trình AI Design Workflow chỉ được tạo khi bắt đầu lesson, theo README của chương trình, nên mình không tạo trước.

---

## Brief 1: Safe reuse of an external skill or repo (cập nhật Lesson 5)

```yaml
title: "Lesson 5: Reuse What Others Built (delta)"
type: lesson
audience: private-training
level: intermediate
duration: "90 min (không đổi)"
```

**Purpose.** Sau buổi học, học viên chạy được một lượt kiểm tra ngắn trước khi dùng repo bên ngoài (nguồn, lần cập nhật, license, đánh giá của AI) và nhờ AI coding tool đổi ngữ cảnh của repo sang dự án của mình.

**Lesson hiện có đã bao gồm:** bốn loại dùng lại được, nơi tìm, đọc repo mà không cần đọc code, clone vào folder mới, cheat sheet ở Bridge, giới hạn của việc nhờ AI diễn giải.

**Structure (chỉ phần thay đổi, dùng trong buffer 5 phút):**
1. Theory (c), thêm khoảng 2 phút: nhờ AI chat tool chấm độ tin cậy và an toàn của repo qua một bộ câu hỏi cố định. Nhấn mạnh đây là một lớp kiểm tra, không phải lớp duy nhất (khớp với Limitations đã có).
2. Bridge: thêm một dòng vào cheat sheet, "Đã nhờ AI đánh giá độ tin cậy và an toàn chưa, và mình hiểu giới hạn của đánh giá đó chưa?".
3. Practice bước 4: thay "đổi tên dự án, ngữ cảnh và một file rules" bằng việc nhờ AI coding tool đổi hàng loạt tên và ngữ cảnh trong toàn repo, rồi học viên kiểm tra kết quả. Lý do: repo template có nhiều file nên sửa tay dễ sót.
4. Limitations hoặc Close: thêm một đoạn ngắn nói rằng trong môi trường doanh nghiệp thường không được cài skill từ bên ngoài vào repo của công ty; công ty hay tự dựng skill, agent và template nội bộ. Học viên thử trong repo cá nhân với dữ liệu mẫu.

**Learning objectives (sửa hai mục hiện có).**
- Mục 3: thêm "và nhờ AI chấm độ tin cậy, nêu được giới hạn của đánh giá đó".
- Mục 5: thêm "bằng cách nhờ AI đổi ngữ cảnh, rồi kiểm tra kết quả".

**Key decisions.**
- Không thêm khung "5 bước" mới, vì lesson đã có luồng tương đương. Chỉ ghép phần còn thiếu.
- Không dùng các ví dụ sự cố cụ thể của đồng nghiệp hoặc công ty, vì là chuyện của bên thứ ba và không kiểm chứng được.
- Số liệu về rủi ro skill dùng lại từ mục Sources của brief Lesson 5, vẫn `[to confirm]` bằng báo cáo gốc trước khi đưa lên slide.
- Sync: sửa lesson thì sửa slide outline trong cùng lượt (CLAUDE.md). Slide count và timing dự kiến không đổi, `[to confirm]` khi viết.

**Open questions for Winnie.**
1. Có đặt tên "5 bước" trên cheat sheet không, hay giữ tên hiện tại?
2. Bộ câu hỏi nhờ AI chấm độ tin cậy do Winnie viết hay lấy từ nguồn ngoài?

---

## Brief 2: "Prompt, don't hand-edit" và hành vi người dùng trên prototype đã publish

### 2a. Cập nhật Lesson 4 (Publish It)

```yaml
title: "Lesson 4: Publish It (delta)"
type: lesson
audience: private-training
level: intermediate
duration: "không đổi"
```

**Purpose.** Học viên hiểu vì sao thay đổi folder và file nên làm qua prompt thay vì sửa tay, và biết cách xử lý khi link GitHub Pages mở không đúng trang.

**Structure (chỉ phần thay đổi):**
1. Thêm quy tắc vào phần `CONTRIBUTING.md` đã có: tạo và đổi tên folder, file qua prompt; sửa tay làm AI và lịch sử thay đổi không còn khớp nhau.
2. Thêm một dòng vào phần xử lý sự cố của Make It Live: link mở sai trang thì nhờ AI trỏ đúng file HTML của prototype (thường là `index.html`), hoặc chỉ rõ file cần mở, rồi kiểm tra lại.

**Key decisions.** Lesson 4 đang có `CONTRIBUTING.md` và phần "AI-tool shortcut", nên đây là mở rộng chứ không đổi cấu trúc. Chưa tìm thấy `index.html` được nhắc tới trong lesson hiện có, `[to confirm]` khi viết.

**Open question.** Quy tắc "không sửa tay" có tuyệt đối không? Winnie kể mình từng sửa tay và mất lịch sử, nên chưa rõ cần nói đây là quy tắc cứng hay mặc định tốt.

### 2b. Block mới trong `refine-and-test`: nhờ AI ghi nhận hành vi người dùng

```yaml
title: "Refine and test: collect behaviour from a live prototype (block)"
type: lesson-block
audience: ux-class
level: intermediate
duration: "20 đến 25 phút trong 90 phút"
```

**Purpose.** Học viên gửi prototype đã publish cho vài người dùng thật, nhờ AI thêm cách ghi nhận click, nơi người dùng bỏ dở và form đã gửi, rồi đọc kết quả xuất ra thành markdown hoặc bảng.

**Structure (đề xuất):**
1. Open, 3 phút: một prototype đã có link live nhưng chưa ai biết người dùng làm gì với nó.
2. Theory, 8 phút: dữ liệu hành vi trả lời được câu hỏi nào (người dùng làm gì) và không trả lời được câu hỏi nào (vì sao); cách đặt câu hỏi cho AI để ghi đúng sự kiện cần đo.
3. Practice, 10 phút: học viên viết ba sự kiện cần đo, nhờ AI coding tool thêm vào prototype, publish lại, tự đóng vai người dùng để kiểm tra có ghi được không.
4. Close, 3 phút: đọc kết quả và nêu một giả thuyết cần kiểm chứng thêm.

**Learning objectives.**
1. Phân biệt được dữ liệu hành vi và lý do của hành vi.
2. Đặt được ba sự kiện cần đo từ một giả thuyết.
3. Kiểm tra được dữ liệu thu về có đúng sự kiện đã định nghĩa không.

**Key decisions.**
- Manual before AI: học viên tự viết sự kiện cần đo trước khi nhờ AI.
- Không dạy dựng backend; lesson dùng nhãn chung "AI coding tool" và "dịch vụ ghi nhận sự kiện".
- Dữ liệu người dùng thật chỉ thu khi có người đồng ý tham gia; không thu thông tin cá nhân. Nhắc lại phần data safety của lesson `design-process-with-ai`.

**`[to confirm]` bắt buộc trước khi viết lesson.**
- Một trang GitHub Pages là trang tĩnh, nên không tự lưu được dữ liệu. Cách thu dữ liệu trong ví dụ gốc (dịch vụ nào, xuất ra file thế nào) chưa rõ, cần Winnie xác nhận.
- Quy định về đồng ý của người dùng khi ghi hành vi (bản đã publish công khai).
- Mọi điều lesson nói về cách ghi nhận sự kiện là cách làm của Winnie, không có nghiên cứu hỗ trợ, trừ khi tìm thêm nguồn.

**Open questions for Winnie.**
1. Công cụ nào đã dùng để thu sự kiện trong ví dụ gốc?
2. Block này nên nằm trong `refine-and-test` hay thành bài bonus riêng ở arc private training?

---

## Brief 3: Cross-check sessions against hypotheses (guide mới)

```yaml
title: "Record every working session, then cross-check it against your hypotheses"
type: guide
audience: ux-class | private-training
level: intermediate
duration: "đọc 15 phút, thực hành 30 phút"
```

**Purpose.** Học viên ghi âm các buổi stakeholder, interview và test với sự đồng ý của người tham gia, đưa transcript cho agent đối chiếu với các giả thuyết đã có, rồi tự kiểm tra từng kết luận trước khi dùng.

**Structure (đề xuất):**
1. Vì sao: map thủ công từ transcript sang giả thuyết chậm và dễ sót; AI đối chiếu nhanh nhưng có thể gán sai.
2. Chuẩn bị: một danh sách giả thuyết có đánh số (từ giai đoạn Define), xin phép ghi âm, làm sạch và ẩn danh transcript trước khi đưa cho AI.
3. Đối chiếu: nhờ agent chỉ ra, với mỗi giả thuyết, những đoạn transcript ủng hộ, phản bác, hoặc không đề cập; yêu cầu trích nguyên văn kèm mốc thời gian.
4. Kiểm tra: học viên đọc lại mọi đoạn trích, loại các kết luận không có trích dẫn, và ghi lại giả thuyết nào chưa có bằng chứng.
5. Lưu: kết quả vào insight pool của case folder, để các giai đoạn sau dẫn chiếu.

**Learning objectives.**
1. Chuẩn bị được transcript an toàn để đưa cho AI (đã ẩn danh, có sự đồng ý).
2. Viết được yêu cầu buộc AI trích nguyên văn và nêu cả bằng chứng phản bác.
3. Phát hiện được ít nhất một kết luận của AI không có căn cứ trong transcript.

**Key decisions.**
- Manual before AI: học viên tự đối chiếu một giả thuyết bằng tay trước, rồi so với kết quả của AI.
- Chỉ nói đây là cách làm của Winnie; chưa gắn nghiên cứu nào. Nếu cần số liệu về độ chính xác của AI khi phân tích định tính, phải tìm nguồn (tác giả, năm, cỡ mẫu) trước khi đưa vào.
- Dẫn chiếu tới phần data safety của `design-process-with-ai` thay vì lặp lại.
- Giữ ví dụ ở mức generic; không dùng transcript thật của mentee.

**Open questions for Winnie.**
1. Có muốn thành guide hay một block trong `refine-and-test`?
2. Quy trình ghi âm và xin phép trong công ty của học viên khác nhau, nên guide chỉ nêu nguyên tắc hay cho mẫu lời xin phép?

---

## Sources

- Brief 1: mục Sources trong `lesson-5-reuse-what-others-built-brief.md` (nguồn rủi ro skill, còn `[to confirm]`).
- Brief 2a: `lesson-3-4-stub.md`, `lesson-4-slide-outline.md`.
- Brief 2b và 3: cách làm của Winnie, chưa có nguồn nghiên cứu. Cần tìm nguồn trước khi nêu bất kỳ con số nào.
- Nguồn gốc: một buổi private training (đã ẩn danh theo WF-2).
