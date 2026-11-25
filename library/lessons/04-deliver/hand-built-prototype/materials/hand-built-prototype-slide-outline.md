# Slide Deck Outline: Hand-Built Prototype

> **Source of truth:** `hand-built-prototype-lesson.md`
> All content changes (activities, concepts, examples, timing) must be made there first, then reflected here.
> This file contains only slide-specific concerns: layout types, visual hints, kickers, structure, and speaker notes.

---

## Session metadata

| Field | Value |
|---|---|
| Session title | Hand-Built Prototype |
| Session subtitle | Nối màn hình thành flow, rồi để người khác bấm thử |
| Instructor | Winnie Nguyen |
| Program | Standalone. Follows Design System, precedes [to confirm] |
| Level | Junior |
| Year | 2026 |
| Previous session | Design System. Output: tokens, components and rules for the chosen concept |
| Next session | [to confirm] |
| Running example | Đặt lịch hẹn (task trong Practice Dataset), hoặc task của học viên |
| Cover photo | Hai bàn tay cầm điện thoại, màn hình đang bấm qua một luồng đặt lịch. Người xem thấy một thao tác đang được thử, không chỉ được xem |
| Style reference | `../assets/style-reference-schematic.png` (chưa có, [to confirm]) |

---

## Visual language

**Bài này dạy cách nối và thử, nên slide phải được nhìn, không chỉ đọc.** Mỗi khái niệm dùng một specimen schematic: khung xám, thanh xám cho chữ, mũi tên sienna cho kết nối.

**SCHEMATIC** cho cơ chế: flow, kết nối, state. **REAL** cho ảnh hoặc màn hình thật. Không trộn hai register trong một slide.

Specimen dùng các token của Design System: `--ink-ghost` cho thanh chữ, `--ink` cho nút chính, `--sienna` cho mũi tên và annotation.

---

## Slides

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Deliver
- Title: Hand-Built\n*Prototype*
- Subtitle: Nối màn hình thành flow, rồi để người khác bấm thử.
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer at NAB
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: hai bàn tay cầm điện thoại, màn hình là một luồng đặt lịch, ánh sáng ấm
- Speaker notes:
  - Buổi này học cách dựng prototype bằng tay trong Figma.
  - Đầu ra là một flow bấm được và một câu hỏi test rõ ràng.
  - Học viên đã biết Figma cơ bản từ bài UI Foundations.
- 🎨 Visual hint: Cover layout, fixed. White left panel with year line, stage label, title (accent on line 2) and subtitle. Right panel is the real photo with dark gradient overlay, name and three credential lines bottom-left.

---

### AGENDA
- Kicker: Agenda
- Title: Nội dung\n*buổi học*
- Lines:
  - 01 · Flow before connections
  - 02 · Connections
  - 03 · Smart Animate and state
- Speaker notes:
  > Ba phần lý thuyết, sau đó thực hành trên một task.
- 🎨 Visual hint: TYPOGRAPHIC. Ba dòng số lớn, số màu tím italic, tên phần tiếng Anh màu ink. Khớp đúng tên các SECTION DIVIDER.

---

### STATEMENT · Mở đầu
- Kicker: Mở đầu
- Title: Bấm thử trước khi kết luận
- On-slide: Một prototype lỗi trông vẫn đúng cho đến khi có người bấm vào nó.
- Speaker notes:
  - Trước khi học cách nối, xem một prototype có ba lỗi.
  > Thử tự bấm qua prototype này. Chỗ nào bạn khựng lại là chỗ có lỗi.
  - Lỗi thứ nhất: một màn không có kết nối đi tiếp.
  - Lỗi thứ hai: flow không có starting point.
  - Lỗi thứ ba: một nút chỉ chạy khi bấm lần hai.
  - Nhìn bằng mắt, prototype này không có gì sai rõ ràng. Lỗi chỉ lộ ra khi có người bấm.
- Ví dụ: bản nháp (prototype lỗi có ba vấn đề, minh họa trong lesson, Open)
- Câu hỏi hay gặp: Không cần xem prototype này trong Figma. Chỉ cần nhớ ba loại lỗi.
- 🎨 Visual hint: TYPOGRAPHIC. Một dòng statement lớn, không có hình.

---

### SECTION DIVIDER · 01
- Num: 01
- Kicker: Chuyển phần
- Title: Flow before\n*connections*
- Sub: Thứ tự làm việc quyết định prototype có đúng không.
- Speaker notes:
  > Flow trước, kết nối sau. Thứ tự này quyết định prototype có đúng không.
- 🎨 Visual hint: SECTION DIVIDER layout on `--paper-deeper`, big num 01 top-left, title two lines with accent on line 2.

---

### NUMBERED · Định nghĩa
- Kicker: Định nghĩa
- Title: Hand-built prototype\n*là gì?*
- On-slide:
  - What: prototype dựng bằng tay trong Figma.
  - Gồm: frame, kết nối, transition và state.
  - Why: mỗi kết nối có lý do của bạn đằng sau.
  - Nếu thiếu: prototype chạy được nhưng không ai biết vì sao.
  - When: khi cần trả lời câu hỏi người dùng có đi qua flow không.
  - Không cần khi: bạn chỉ muốn xem chuyển động.
- Speaker notes:
  - Hand-built prototype là prototype bạn tự nối từng kết nối trong Figma.
  - Khác với prototype do công cụ sinh ra, mỗi kết nối đều phải có lý do.
  > Khi có lỗi, bạn biết tìm ở đâu, vì bạn đã tự làm từng bước.
  - Dùng khi câu hỏi là người dùng có đi qua được flow không.
  - Không cần khi câu hỏi là chuyển động có tạo cảm giác tốt không.
- Ví dụ: có (đặt lịch hẹn, task trong Practice Dataset)
- 🎨 Visual hint: NUMBERED, sáu hàng ngắn với nhãn What, Gồm, Why, Nếu thiếu, When, Không cần khi; icon nhỏ góc phải.

---

### PROCESS · Cách làm
- Kicker: Cách làm
- Title: Năm bước từ flow đến test
- On-slide: Vẽ flow · Dựng màn · Nối · Bấm thử · Test với người khác
- Speaker notes:
  - Bước một là vẽ flow của task trên giấy hoặc sơ đồ, liệt kê từng bước người dùng làm.
  - Bước hai là dựng từng màn tương ứng với bước đó.
  - Bước ba là nối các màn theo flow.
  - Bước bốn là tự bấm thử từ đầu đến cuối.
  > Bước năm là đưa cho một người khác thử, và chỉ quan sát.
- Ví dụ: có (task đặt lịch hẹn: chọn dịch vụ, chọn giờ, nhập thông tin, xác nhận, nhận mã)
- 🎨 Visual hint: PROCESS, năm bước trên track `repeat(5,1fr)`, bước "Nối" đang active (sienna).

---

### COMPARE · So sánh
- Kicker: So sánh
- Title: Low hay high fidelity?
- On-slide:
  - Low: kiểm tra cấu trúc và thứ tự các bước.
  - High: thấy chuyển động và state.
  - Low không thể hiện được animation.
  - High tốn công khi flow còn sai.
- Speaker notes:
  - Low fidelity là khung và thanh xám. Đủ để kiểm tra flow có đi qua được không.
  - High fidelity có animation, state và overlay. Nên đến sau khi cấu trúc đã ổn.
  > Dựng high fidelity quá sớm là đánh bóng một giải pháp chưa được kiểm chứng.
  - Chọn mức theo câu hỏi bạn cần trả lời, không theo thói quen.
- Ví dụ: bản nháp (hai bản prototype cùng một flow đặt lịch, một bản low và một bản high)
- Câu hỏi hay gặp: Có cần high fidelity để test không? Không, nếu câu hỏi chỉ là flow có đi qua được không.
- 🎨 Visual hint: COMPARE, hai cột: low với nhãn pos (sage), high với nhãn neg (sienna) theo nội dung.

---

### STATEMENT · Câu hỏi lớp (Check 1)
- Kicker: Câu hỏi cho lớp
- Title: Vẽ flow hay nối trước?
- On-slide: Bạn sẽ làm gì trước, và vì sao?
- Speaker notes:
  > Bạn sẽ vẽ flow trước hay nối trước? Vì sao?
  - Nối trước dễ bỏ sót bước, và chỉ thấy khi có người bấm.
- Ví dụ: không cần
- 🎨 Visual hint: TYPOGRAPHIC. Một câu hỏi lớn ở giữa, không có hình.

---

### SECTION DIVIDER · 02
- Num: 02
- Kicker: Chuyển phần
- Title: *Connections*
- Sub: Mỗi mũi tên trong Figma trả lời một câu hỏi.
- Speaker notes:
  > Mỗi kết nối có ba thành phần, và mỗi flow cần một starting point.
- 🎨 Visual hint: SECTION DIVIDER layout on `--paper-deeper`, big num 02.

---

### NUMBERED · Định nghĩa
- Kicker: Định nghĩa
- Title: Trigger, action, transition
- On-slide:
  - Trigger: hành động của người dùng.
  - Action: điều xảy ra sau đó.
  - Transition: cách màn chuyển.
- Speaker notes:
  - Trigger là click, hover, drag hoặc bấm phím.
  - Action là đi đến frame, mở overlay, đóng overlay hoặc quay lại.
  - Transition là Instant, Dissolve, Smart Animate hoặc các kiểu trượt.
  > Đọc một kết nối theo thứ tự: người dùng làm gì, việc gì xảy ra, và màn chuyển thế nào.
- Ví dụ: bản nháp (nút Xác nhận: trigger là click, action là đi đến màn Đã đặt lịch, transition là Instant)
- 🎨 Visual hint: NUMBERED, ba cột: Trigger, Action, Transition, mỗi cột một số lớn màu sienna.

---

### DIAGRAM · Starting point và flow
- Kicker: Cách làm
- Title: Starting point và flow
- On-slide: Một starting point cho mỗi flow, trên một frame cấp cao nhất.
- Speaker notes:
  - Mỗi flow cần một starting point.
  - Một frame có thể thuộc nhiều flow, nhưng chỉ có một starting point.
  > Thiếu starting point, một số công cụ test báo lỗi hoặc không chạy được prototype.
  - Đặt tên cho starting point để dễ tìm khi file có nhiều flow.
- Ví dụ: có (flow đặt lịch hẹn có ba frame và một frame không có kết nối)
- Hình: `../assets/hbp-starting-point-flow.html` (sơ đồ đã vẽ, cần xuất SVG khi lên slide)
- 🎨 Visual hint: SCHEMATIC. Ba khung xám nối bằng mũi tên sienna, một marker starting point ở khung đầu, một khung cuối bị đánh dấu thiếu kết nối bằng viền đứt.

---

### COMPARE · Overlay hay màn mới
- Kicker: So sánh
- Title: Overlay hay màn mới?
- On-slide:
  - Overlay: menu, hộp xác nhận, tooltip.
  - Màn mới: người dùng thật sự chuyển sang một màn khác.
  - Overlay giữ người dùng ở màn hiện tại.
  - Màn mới thay đổi toàn bộ ngữ cảnh.
- Speaker notes:
  - Overlay hiện nội dung trên màn hiện tại mà không rời màn đó.
  - Dùng overlay cho menu, hộp xác nhận, tooltip và bottom sheet.
  > Nếu người dùng không rời khỏi màn, đừng nối sang một frame mới.
  - Open Overlay giúp giảm thao tác lặp khi bạn nối nhiều overlay giống nhau.
- Ví dụ: có (hộp xác nhận sau khi bấm Xác nhận)
- Hình: `../assets/hbp-overlay-vs-screen.html`
- 🎨 Visual hint: COMPARE, hai cột: overlay với nhãn pos, màn mới với nhãn neg, mỗi cột có một sơ đồ nhỏ.

---

### STATEMENT · Câu hỏi lớp (Check 2)
- Kicker: Câu hỏi cho lớp
- Title: Nút mở hộp xác nhận
- On-slide: Chọn action nào?
- Speaker notes:
  > Một nút mở một hộp xác nhận, bạn chọn action nào?
  - Đáp án: open overlay, không phải đi đến một frame mới.
- Ví dụ: không cần
- 🎨 Visual hint: TYPOGRAPHIC. Một câu hỏi lớn ở giữa.

---

### SECTION DIVIDER · 03
- Num: 03
- Kicker: Chuyển phần
- Title: Smart Animate\n*and state*
- Sub: Smart Animate khớp layer, không đọc nội dung màn hình.
- Speaker notes:
  > Tên layer quyết định chuyển động, còn variant giữ state của component.
- 🎨 Visual hint: SECTION DIVIDER layout on `--paper-deeper`, big num 03.

---

### NUMBERED · Quy tắc
- Kicker: Quy tắc
- Title: Giữ Smart Animate chạy đúng
- On-slide:
  - Tên layer giống nhau giữa hai frame.
  - Cùng vị trí trong hierarchy.
  - Nhân bản frame thay vì dựng lại.
  - Ẩn layer bằng opacity 0%.
- Speaker notes:
  - Smart Animate khớp layer theo tên và vị trí trong hierarchy.
  - Nhân bản frame giữ tên nhất quán giữa các màn.
  > Để ẩn một layer, đặt opacity về 0%, đừng tắt visibility.
  - Giữ mọi layer ở cả hai frame, kể cả layer không hiện ở frame kia.
- Ví dụ: có (nút đổi màu từ trạng thái thường sang trạng thái đã chọn)
- 🎨 Visual hint: NUMBERED, bốn mục trong lưới 2 cột, số màu sienna.

---

### DIAGRAM · Viền tím trong tab Prototype
- Kicker: Cách làm
- Title: Kiểm tra khớp layer
- On-slide: Viền tím là layer Figma sẽ khớp. Không có viền là không khớp.
- Speaker notes:
  - Mở tab Prototype để xem layer nào được khớp.
  > Hai frame của một nút có layer "Label" và "Text" ở hai bên. Smart Animate khớp layer nào?
  > Nếu layer không có viền tím, Smart Animate sẽ không chuyển động cho layer đó.
  - Kiểm tra trước khi test, đừng đợi người khác tìm ra lỗi.
- Ví dụ: có (hai frame của nút, một layer Label khớp, một layer Text không khớp vì tên khác nhau)
- Hình: `../assets/hbp-smart-animate-match.html`
- 🎨 Visual hint: SCHEMATIC. Hai khung xám cạnh nhau. Các layer khớp có viền tím đứt, một layer có tên khác không có viền.

---

### STATEMENT · Giới hạn
- Kicker: Giới hạn
- Title: Đừng bắt Smart Animate làm mọi thứ
- On-slide: Đổi nội dung text và đổi hẳn một vật thể không được chuyển động.
- Speaker notes:
  - Smart Animate không chuyển động được việc thay đổi nội dung text.
  - Khi có nhiều thay đổi cùng lúc, chuyển động có thể bị giật.
  > Dùng Smart Animate cho chuyển động chính, và transition đơn giản cho phần còn lại.
- Ví dụ: không cần
- 🎨 Visual hint: TYPOGRAPHIC. Một câu statement lớn ở giữa.

---

### DIAGRAM · Variant thay cho frame rời
- Kicker: Cách làm
- Title: Variant thay cho frame rời
- On-slide: Checkbox: hai variant, hai kết nối.
- Speaker notes:
  - Để dựng các state của một component, đặt chúng trong cùng một component set.
  > Với checkbox, bạn chỉ cần hai variant và hai kết nối, không cần một frame cho mỗi state.
  - Chỉ nối được các variant trong cùng một component set.
  - Tên variant có thể khác nhau, nhưng layer bên trong phải có tên nhất quán.
  - Nếu state bị kéo sang màn khác, bật Reset component state.
- Ví dụ: có (checkbox trong form đặt lịch)
- Hình: `../assets/hbp-variant-checkbox.html`
- 🎨 Visual hint: SCHEMATIC. Hai khung checkbox (không chọn, đã chọn), nối hai chiều bằng mũi tên sienna, nhãn variant nhỏ bằng mono.

---

### NUMBERED · Lỗi hay gặp
- Kicker: Lỗi hay gặp
- Title: Năm lỗi làm test thất bại
- On-slide:
  - Không có starting point.
  - Dead end: màn không có kết nối đi tiếp.
  - Chỉ có happy path, thiếu lỗi và trạng thái trống.
  - Hover trên màn hình cảm ứng không chạy.
  - Người xem thiếu quyền truy cập.
- Speaker notes:
  - Dead end làm tăng số lần bấm nhầm và làm người test bối rối.
  - Thiếu error state làm prototype không cho engineer và người dùng thấy đầy đủ flow.
  > Trước khi tuyển người test, tự đi hết mọi đường chính và đường biên.
  - Khi test thất bại, hỏi người test: bạn kỳ vọng điều gì xảy ra ở đây?
- Ví dụ: bản nháp (prototype đặt lịch thiếu trạng thái giờ đã kín)
- 🎨 Visual hint: NUMBERED, năm mục trong lưới 3 cột, số màu sienna.

---

### MILESTONE · Thực hành
- Kicker: Thực hành
- Num: 35 phút
- Title: Dựng flow và test nhanh
- Sub: Vẽ flow, nối, dựng state, test với một bạn học. Làm liền một mạch.
- Speaker notes:
  > Thực hành 35 phút, làm liền một mạch, không dừng giữa chừng.
  - Bước một: vẽ flow, 5 phút.
  - Bước hai: nối flow và thêm một overlay, 12 phút.
  - Bước ba: dựng state bằng variant, 8 phút.
  - Bước bốn: test nhanh với một bạn học, 10 phút. Chỉ quan sát, không giải thích.
  - Dự phòng 2 phút ở cuối buổi.
- 🎨 Visual hint: MILESTONE, nền sienna, num "35 phút" lớn.

---

### PRACTICE · Bài tập về nhà
- Kicker: Practice
- Title: Bài tập *về nhà*
- Card 1 · Dựng flow:
  - Flow ba đến năm màn cho một task.
  - Starting point, một overlay, một component có hai variant.
  - Một đường lỗi và một trạng thái trống.
  - Tên layer nhất quán cho Smart Animate.
- Card 2 · Nộp và test:
  - Link Figma kèm starting point đã đặt tên.
  - Câu hỏi test đã viết trước khi test.
  - Kết quả một lần test với một người.
  - Ghi chú: lỗi nào là lỗi thiết kế, lỗi nào là lỗi prototype.
- Speaker notes:
  - Thời lượng khoảng hai giờ, làm ở nhà.
  > Nộp link Figma và câu hỏi test trước buổi tiếp theo.
  - Chi tiết và tiêu chí chấm nằm trong file practice.
- 🎨 Visual hint: TWO CARDS, mỗi card có icon, h3 và đúng bốn bullet.

---

### STATEMENT · Kết
- Kicker: Kết
- Title: Prototype trả lời *một* câu hỏi
- On-slide: Viết câu hỏi test trước khi bấm thử.
- Speaker notes:
  - Trước khi nối bất kỳ kết nối nào, hãy viết câu hỏi bạn cần trả lời.
  > Câu hỏi đó quyết định mức fidelity, flow nào cần dựng, và câu hỏi test nào sẽ được đặt.
  - Bài tập về nhà là phần nối tiếp của buổi này.
- Ví dụ: không cần
- 🎨 Visual hint: TYPOGRAPHIC. Một câu statement lớn ở giữa.

---

### Q&A
- Kicker: Bạn muốn hỏi về
- Title: Hỏi đáp
- Speaker notes:
  > Câu hỏi về task của bạn là câu hỏi đáng hỏi nhất hôm nay.
- 🎨 Visual hint: Q&A layout, identical in every lesson. Left panel solid yellow with `Q&A`; right panel with three cards: `Nội dung hôm nay`, `Hướng đi nghề nghiệp của design`, `Khoá học`.

---

### END
- Kicker: Hẹn gặp lại
- Title: Cảm ơn bạn
- Sign: Winnie Nguyen
- Speaker notes:
  - Kết thúc buổi học.
- 🎨 Visual hint: END layout on `--paper-deeper`, kicker sienna mono, title italic.

---

slide_count: 24
