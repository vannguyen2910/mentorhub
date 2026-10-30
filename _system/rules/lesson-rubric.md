# Lesson Rubric: tiêu chí chấm thiết kế bài giảng

File chuẩn cho agent judge. Chỉnh file này để đổi cách chấm, không cần sửa agent. Rubric viết chung, dùng được cho bất kỳ người dạy hay chương trình nào. Đây là **bản nháp v0.1**, chờ duyệt wording và hiệu chỉnh bằng hai lesson chạy thử.

Phạm vi: chấm **thiết kế bài** (file lesson, slide outline, practice sheet). Chưa chấm cách giảng; việc đó cần transcript hoặc recording và do người quyết định.

## Nguồn và giới hạn

- Lớp A dựa trên năm nguyên lý của Merrill (First Principles of Instruction). Mô tả từng mức được viết từ hiểu biết chung, **chưa đối chiếu nguồn gốc**. Người dùng cần rà wording trước khi tin điểm.
- Cấu trúc bốn mức mượn từ Danielson Framework (Unsatisfactory, Basic, Proficient, Distinguished).
- Lớp B lấy từ checklist teach-ability của skill `review-mentoring`.
- Nghiên cứu về AI judge cho thấy judge hay chấm quá tay, thiên vị khen và giải thích mơ hồ. Vì vậy quy trình bên dưới bắt buộc evidence và liệt kê vấn đề trước khi chấm. Judge dùng để phát hiện vấn đề sớm, không thay phán đoán của người dạy.

## Quy trình bắt buộc cho agent

1. Đọc file lesson, slide outline, practice sheet (nếu có) và các rule của dự án (nếu có).
2. Chạy Lớp C (kiểm tra bằng script) và giữ nguyên kết quả.
3. Với mỗi tiêu chí ở Lớp A và B, **trích evidence trước**: nguyên văn một câu, tên slide hoặc số phút, kèm vị trí (file, slide, heading).
4. **Liệt kê toàn bộ vấn đề** theo độ nghiêm trọng (Critical, Improvement, Note) trước khi cho điểm.
5. Chấm từng tiêu chí. Bắt đầu từ mức 2 và chỉ nâng khi có evidence.
6. Không có điểm tổng.

## Quy tắc chống chấm quá tay

- Không có evidence thì không được cho trên mức 2.
- Mức 4 phải chỉ ra điều cụ thể vượt mức 3, không chỉ là "tốt hơn".
- Nếu mọi tiêu chí đạt từ mức 3 trở lên, báo cáo phải nêu rõ đã tìm lỗi ở đâu và không thấy gì, rồi dừng. Không bịa lỗi cho đủ.
- Không mở đầu bằng lời khen. Phần "đang hoạt động tốt" ngắn và nằm cuối.
- Không đưa tên người học, tên tổ chức hay tên sản phẩm cụ thể vào báo cáo.
- Không tự điền ví dụ như thể đã có thật. Nếu gợi ý, gắn nhãn `bản nháp`.

---

## Lớp A: Sư phạm theo Merrill (agent chấm)

Mỗi tiêu chí có bốn mức: 1 Thiếu, 2 Cơ bản, 3 Đạt, 4 Xuất sắc.

### A1. Task-centered

Bài xoay quanh một task thật, không phải một danh sách khái niệm.

| Mức | Mô tả |
|---|---|
| 1 | Khái niệm đứng riêng, không có tình huống thật. Ví dụ rời rạc hoặc đổi case giữa bài. |
| 2 | Có một tình huống, nhưng chỉ ở phần mở đầu hoặc ở vài slide. |
| 3 | Một case xuyên suốt từ mở bài đến activity. Khái niệm nào cũng được gắn lại với case. |
| 4 | Như mức 3, và case tăng dần độ phức tạp qua các phase. Cuối bài người học làm một phiên bản của chính task đó. |

### A2. Activation

Bài gợi lại kinh nghiệm hoặc kiến thức có sẵn của người học trước khi dạy cái mới.

| Mức | Mô tả |
|---|---|
| 1 | Vào thẳng định nghĩa, không hỏi gì người học. |
| 2 | Có câu hỏi mở đầu nhưng chung chung, và câu trả lời không được dùng lại. |
| 3 | Có bước khiến người học nhớ lại kinh nghiệm cụ thể liên quan, và bài quay lại dùng câu trả lời đó. |
| 4 | Như mức 3, và bước này làm lộ khoảng trống: người học tự thấy cách làm hiện tại chưa đủ trước khi khái niệm xuất hiện. |

### A3. Demonstration

Người học thấy cách làm trước khi tự làm.

| Mức | Mô tả |
|---|---|
| 1 | Chỉ định nghĩa hoặc mô tả, không có mẫu. |
| 2 | Có ví dụ nhưng đặt sau khái niệm, hoặc chỉ cho thấy kết quả cuối mà không thấy cách làm. |
| 3 | Ví dụ cụ thể đi trước, khái niệm đặt tên sau. Có mẫu làm từng bước để bắt chước. |
| 4 | Như mức 3, và có đối chiếu làm đúng với làm sai, hoặc hai ngữ cảnh khác nhau, để người học không học thuộc một case. |

### A4. Application

Người học luyện đúng kỹ năng vừa được dạy.

| Mức | Mô tả |
|---|---|
| 1 | Không có activity, hoặc activity chỉ là nghe và ghi chép. |
| 2 | Có activity nhưng luyện kỹ năng gần giống, hoặc không có tiêu chí hoàn thành và feedback. |
| 3 | Activity luyện đúng kỹ năng vừa dạy. Có hướng dẫn rõ, tiêu chí hoàn thành và cách nhận feedback. |
| 4 | Như mức 3, và có độ khó tăng dần hoặc cơ hội làm lại sau feedback. Thời lượng activity khớp số phút phân bổ. |

### A5. Integration

Người học mang kỹ năng ra khỏi lớp.

| Mức | Mô tả |
|---|---|
| 1 | Bài kết thúc ở slide cuối, không có bước áp dụng ngoài lớp. |
| 2 | Có homework nhưng chung chung, không gắn với công việc hay project thật của người học, hoặc không có sản phẩm kiểm tra được. |
| 3 | Homework yêu cầu áp dụng vào công việc hay project thật của người học, có sản phẩm đầu ra cụ thể và cách trình bày lại. |
| 4 | Như mức 3, và có tiêu chí tự đánh giá hoặc điểm kiểm tra lại sau một thời gian, nối sang buổi sau. |

### A6. Alignment

Mục tiêu, activity và homework cùng trỏ về một năng lực.

| Mức | Mô tả |
|---|---|
| 1 | Mục tiêu, activity và homework nói về các năng lực khác nhau. |
| 2 | Mục tiêu và activity khớp nhưng homework lệch, hoặc mục tiêu mơ hồ nên không kiểm tra được. |
| 3 | Mỗi mục tiêu có ít nhất một activity luyện và một chỗ kiểm tra. Người học nói lại được mình vừa học được gì. |
| 4 | Như mức 3, và mục tiêu viết dưới dạng hành vi quan sát được, đối chiếu thẳng với sản phẩm cuối. |

**Khung milestone (tùy chọn).** Nếu bài dùng khung nhiều mốc như KNOW / DO / SHOW, thêm một câu hỏi vào A6: cả các mốc có mặt và nối nhau không? Thiếu một mốc là vấn đề Critical ở A6, không tạo tiêu chí riêng. Bài không dùng khung này thì bỏ qua.

---

## Lớp B: Dạy được trên lớp (agent chấm)

Nguồn: checklist teach-ability của `review-mentoring`. Dùng bốn mức như Lớp A.

### B1. Sequence và difficulty ramp

| Mức | Mô tả |
|---|---|
| 1 | Có khái niệm được dùng trước khi dạy, hoặc độ khó nhảy bậc khiến người học mới sẽ kẹt. |
| 2 | Thứ tự đúng nhưng có một bước nhảy độ khó chưa được đỡ bằng ví dụ hay activity. |
| 3 | Mỗi khái niệm xuất hiện sau khi nền của nó đã được dạy. Độ khó tăng đều. |
| 4 | Như mức 3, và có điểm kiểm tra hiểu bài ở chỗ dễ kẹt nhất. |

### B2. Pacing so với thời lượng

Đối chiếu nội dung từng slide với số phút của phase trong bảng cấu trúc buổi học. Ước lượng thời gian nói bằng công cụ đếm từ nếu có.

| Mức | Mô tả |
|---|---|
| 1 | Tổng thời lượng ước tính lệch quá 25% so với buổi, hoặc có phase cần gấp đôi thời gian được cấp. |
| 2 | Tổng khớp nhưng một vài phase quá tải hoặc quá thưa. |
| 3 | Mỗi phase có lượng nội dung khớp số phút. |
| 4 | Như mức 3, và lesson có sẵn phương án cắt hoặc kéo dài có thứ tự khi quá giờ. |

### B3. Tải mỗi slide và khả năng liếc

| Mức | Mô tả |
|---|---|
| 1 | Nhiều slide gộp khái niệm, ví dụ và chuyển tiếp vào một. Người giảng phải đọc chữ dày mới biết nói gì tiếp. |
| 2 | Phần lớn slide một ý, nhưng một vài slide làm hai việc một lúc. |
| 3 | Mỗi slide một ý. Liếc một cái biết câu tiếp theo cần nói. |
| 4 | Như mức 3, và layout được chọn đúng với loại nội dung (so sánh, quy trình, cơ chế). |

### B4. Chuyển tiếp

| Mức | Mô tả |
|---|---|
| 1 | Nhiều chỗ chuyển slide không có câu nối trong speaker notes. |
| 2 | Chuyển phase có câu nối, chuyển slide trong cùng phase thì không. |
| 3 | Mọi chỗ chuyển đều có câu nối nói được thành lời. |
| 4 | Như mức 3, và câu nối đồng thời là câu hỏi hoặc gợi mở giữ người học theo kịp. |

### B5. Lesson và outline đồng bộ (phần phán đoán)

Phần cơ học (số slide, timing) nằm ở Lớp C. Lớp này chấm phần ý nghĩa. Chỉ áp dụng khi có cả lesson lẫn outline.

| Mức | Mô tả |
|---|---|
| 1 | Outline dạy một thứ khác với lesson (phase, thứ tự hoặc kết luận khác nhau). |
| 2 | Cùng cấu trúc nhưng một vài ý trong outline không có chỗ dựa trong lesson, hoặc ngược lại. |
| 3 | Lesson là nguồn, outline phản ánh đúng. Không có ý nào chỉ tồn tại ở một bên. |
| 4 | Như mức 3, và mọi số liệu hay trích dẫn dùng trên slide truy ngược được về phần tài liệu tham khảo của lesson. |

---

## Lớp C: Quy tắc cứng (script chạy, agent không chấm)

Agent chạy rồi chép nguyên kết quả vào báo cáo, ghi rõ lệnh đã chạy. Danh sách dưới đây là loại kiểm tra; dự án gắn lệnh cụ thể vào cột bên phải.

| Kiểm tra | Cách chạy |
|---|---|
| Cấu trúc speaker notes, độ dài tiêu đề, kicker, ví dụ còn thiếu, thời gian nói | Script audit outline của dự án (nếu có) |
| Nhất quán tên và số giữa các file phụ thuộc | Script consistency của dự án (nếu có) |
| Em dash trong lesson, outline, practice | `grep -nP "\x{2014}" <file>` |
| Tên sản phẩm hoặc công cụ cụ thể mà dự án muốn thay bằng nhãn chung | grep theo danh sách của dự án |
| Tên người học trong nội dung dùng chung | grep theo danh sách tên người học của dự án |
| Tên tổ chức trong nội dung công khai | grep theo danh sách của dự án |
| Cụm từ cần tránh theo hướng dẫn giọng văn của dự án | Đối chiếu bảng từ của dự án |

Ghi chú: kết quả khớp trong phần tài liệu tham khảo hoặc trích nguồn học thuật có thể là ngoại lệ chấp nhận được. Agent đánh dấu để người dạy quyết, không tự bỏ qua.

---

## Mẫu báo cáo

Ghi vào `materials/_review/judge-YYYY-MM-DD.md` cạnh lesson. Viết bằng ngôn ngữ của lesson, ngắn.

```
# Judge: <tên lesson> (YYYY-MM-DD)

## Top 3 issues
1. <mức Critical> <vấn đề> | evidence: "<trích>" (<vị trí>) | sửa: <đề xuất>
2. ...
3. ...

## All issues
Critical / Improvement / Note, mỗi dòng có evidence.

## Scores
| Tiêu chí | Mức | Evidence chính |
|---|---|---|

## Script results (Layer C)
Lệnh đã chạy và kết quả nguyên văn.

## What works
Hai đến ba dòng, ở cuối.
```

## Hiệu chỉnh (làm sau khi có agent)

Chạy trên hai lesson: một lesson đã hoàn chỉnh và một lesson còn draft. Kỳ vọng: judge cho điểm cao hơn rõ rệt ở lesson hoàn chỉnh và chỉ ra đúng các phần còn thiếu ở bản draft. Nếu không phân biệt được hai lesson, chỉnh mô tả mức trong file này trước khi tin judge.
