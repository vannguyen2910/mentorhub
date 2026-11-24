---
title: "UI Foundations: Building in Figma"
lesson_file: "ui-foundations-figma-lesson.md"
level: "Beginner"
slide_count: 48
duration: "90 min"
status: draft
built_deck: "https://claude.ai/artifact/LGLDrbqwhnSiXAHq955s1F"
last_synced: 2026-11-24
---

## Session metadata

| Field | Value |
|---|---|
| Program | Private training |
| Track / session | Buổi dựng trên Figma, 90 phút, một học viên làm trên file của mình |
| Stage | Develop |
| Prior session | UI Fundamentals. Output: chosen-concept.png, decision sheet, token set |
| Next session | Design System |
| Running example | File mẫu "xấu" (màn hình "Lịch hẹn của tôi" với 8 lỗi) ở đầu mỗi nhiệm vụ; concept của học viên ở phần còn lại |

**Slide structure:** 48 slide. Thứ tự: COVER, AGENDA, sáu phần (mỗi phần mở bằng SECTION DIVIDER; phần 02 đến 05 kết bằng MILESTONE cho phần làm việc), rồi quick check, PRACTICE và END. Tất cả đều là slide chính. Buổi này là buổi dựng nên không có phần Q&A riêng; câu hỏi được trả lời khi đang làm. Prototype không nằm trong buổi này vì đã có lesson riêng.

---

## Slides

### 01 · COVER · UI Foundations: Building in Figma
- Year: 2026 · Winnie Nguyen
- Stage: Develop
- Title: UI Foundations:\n*Building in Figma*
- Subtitle: Dựng concept của bạn thành file Figma chạy ở hai kích thước
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer at NAB
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: Ảnh thật, một màn hình laptop mở file thiết kế với các frame xếp ngay ngắn, ánh sáng ấm, tập trung
- Speaker notes:
  > Hôm nay mình dựng concept bạn đã chọn thành một file Figma người khác mở lên là hiểu.
  - Bạn đã có concept, decision sheet và token set từ buổi UI Fundamentals, nên hôm nay mình không bàn lại vì sao chọn giá trị nào
  - Buổi này là buổi làm: mình vào việc ngay từ đầu, không có phần demo
  - Bốn việc theo thứ tự: variables, auto layout, component, rồi cho cùng một thiết kế chạy ở hai kích thước
  - Mỗi việc mở bằng vài phút sửa lỗi trên một file mẫu “xấu” trước khi làm trên file của bạn
  > Bạn đã mở file của mình và token set chưa?
- Ví dụ: Không cần. Slide mở đầu.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Cover layout, fixed. White left panel with year line, stage label, title (accent on line 2) and subtitle. Right panel is the real photo with dark gradient overlay, name and three credential lines bottom-left.

---

### 02 · AGENDA · Nội dung buổi học
- Kicker: Agenda
- Title: Nội dung\n*buổi học*
- On-slide:
  - 01
  - File check
  - 02
  - Variables
  - 03
  - Auto layout
  - 04
  - Components
  - 05
  - Breakpoints
  - 06
  - Handoff
- Speaker notes:
  > Sáu phần, và các phần làm việc từ phần hai trở đi đều mở bằng một lỗi thật trên file mẫu.
  - Phần một chỉ kiểm file đã dọn trước buổi, khoảng mười phút
  - Bốn phần sau là bốn nhiệm vụ: mười lăm, hai mươi mốt, hai mươi bốn và mười bốn phút
  - Phần cuối của buổi là sáu phút rà lại, trong đó có ba phút dự phòng
  - Thứ tự này có lý do: auto layout dùng spacing lấy từ variables, và breakpoint dùng mode của chính những variables đó
  > Variables đứng trước auto layout, vì auto layout sẽ lấy khoảng cách từ variables.
- Ví dụ: Không cần. Slide agenda.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Typographic

---

### 03 · SECTION DIVIDER · File check
- Num: 01
- Kicker: Chuyển phần
- Title: File\n*check*
- Sub: Một người lạ mở file, tìm được đường không?
- Speaker notes:
  > Việc đầu tiên không phải dựng gì cả, mà là xem một người lạ có tìm được đường trong file của bạn không.
  - File đã được dọn theo guide gửi trước buổi
  - Mười phút này chỉ kiểm lại kết quả và chốt concept sẽ dựng
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Typographic

---

### 04 · DIAGRAM · File gọn trông thế nào
- Kicker: Cấu trúc
- Title: File gọn trông\n*thế nào*
- On-slide:
  - Năm page, mỗi page một việc
  - Frame đặt tên theo Màn/Thiết-bị
  - Có một chỗ cho bản đã chốt
- Speaker notes:
  > Một designer mở file của đồng nghiệp để dựng tiếp. Trang đầu có ba màn hình tên Frame 1, Frame 1 copy và Frame 1 final 2, cạnh một ghi chú “NHÁP, đừng xoá”.
  - Không ai biết bản nào là bản cuối, nên việc đầu tiên là hỏi lại người làm; đó là một file không tự giải thích được
  - Cấu trúc nhắm tới có năm page: Cover, Components, Screens, Handoff và _Archive
  - Trong Screens, các frame gom theo section và đặt tên theo quy ước Màn/Thiết-bị, ví dụ Booking/Mobile
  - Phép thử: một người lạ mở file và, trong ba mươi giây, tìm được màn hình đang làm, nơi chứa component và bản đã chốt
  - Đây là phần hầu hết giáo trình Figma công khai không dạy riêng, nên mình giữ nó ở đầu buổi
  > File của bạn có qua được phép thử ba mươi giây không?
- Ví dụ: có (file có Frame 1, Frame 1 copy, Frame 1 final 2)
- Câu hỏi hay gặp: Có cần đủ cả năm page không? Page Handoff có thể để trống đến khi có bản chốt; điều quan trọng là mỗi loại việc có một chỗ riêng.
- 🎨 Visual hint: SCHEMATIC. `assets/diagrams/file-structure-clean.html`: cây File, năm page, section Booking và hai frame; Screens nhấn màu cam.

---

### 05 · NUMBERED · Đặt tên cho ba loại thứ
- Kicker: Quy ước
- Title: Đặt tên cho ba loại thứ
- On-slide:
  - Layer: theo vai trò, card, title, cta
  - Variable: color/action/fill
  - Component: Button/Primary/Hover
- Speaker notes:

  > Ba thứ cần tên, và cả ba đều đi theo một nguyên tắc: tên nói vai trò, không nói hình dạng hay giá trị hiện tại.

  - Layer: card, title, cta, thay cho Frame 12 hay Rectangle 3
  - Variable: color/action/fill vẫn đúng khi màu đổi, còn blue-main thì sai ngay lúc đổi
  - Component: Button/Primary/Hover, nhóm trước rồi tới tên và trạng thái, theo cách Figma Help gợi ý
  - Carbon dùng text-primary và button-primary-active; Atlassian dùng color.background.danger.bold.hovered
  - Material 3 và Primer chưa mở được trang gốc nên không trích

  > Tên layer nào trong file của bạn đang nói hình dạng thay cho vai trò?
- Ví dụ: có (file mẫu xấu: Frame 1, Rectangle 3)
- Câu hỏi hay gặp: Quy tắc atomic a/m/o có dạy không? Không, để buổi Design System.
- 🎨 Visual hint: TYPOGRAPHIC. Ba thẻ cùng cấp: Layer, Variable, Component, mỗi thẻ một ví dụ tên.

---

### 06 · MILESTONE · Kiểm file của bạn
- Kicker: Activity
- Num: 10 min
- Title: Kiểm file\n*của bạn*
- Prompt: Tìm màn hình đang làm, nơi chứa component và bản đã chốt trong ba mươi giây. Chốt concept sẽ dựng.
- On-slide: nothing else
- Speaker notes:
  > Bạn tìm giúp mình ba thứ trong file của bạn: màn hình đang làm, nơi chứa component và bản đã chốt.
  - Mười phút, trên file bạn đã dọn trước buổi
  - Mình quét layers panel và danh sách page để xem còn tên mặc định hay frame nháp nằm sai chỗ
  - Concept sẽ dựng là chosen-concept.png đặt cạnh token set của buổi UI Fundamentals
  - Concept còn thô, chưa có chữ thật, thì dựng với nội dung giữ chỗ và ghi lại
  - File chưa dọn xong thì dọn nhanh các lỗi lớn nhất, phần còn lại ghi thành homework
  > Concept nào bạn dựng hôm nay, và token set của nó nằm ở đâu?
- Ví dụ: Không cần. Đây là phần làm việc trên file của học viên.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Milestone layout, sienna background.

---

### 07 · SECTION DIVIDER · Variables
- Num: 02
- Kicker: Chuyển phần
- Title: *Variables*
- Sub: Từ ba mã màu gõ tay đến một giá trị có tên
- Speaker notes:
  > Mình bắt đầu từ chỗ nhỏ nhất: một giá trị chỉ nên được viết ra một lần.
  - Variables là phần mười lăm phút đầu tiên của buổi làm việc
  - Hai collection, ba nhóm giá trị, chưa dạy modes ở đây
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Typographic

---

### 08 · IMAGE · Ba nút cam, ba giá trị
- Kicker: File mẫu
- Title: Ba nút cam,\n*ba giá trị*
- On-slide:
  - File mẫu: ba sắc cam và nhiều xám gần giống nhau, tất cả gõ tay
- Speaker notes:
  > Trên màn hình này có ba nút cam. Nhìn bằng mắt thì cùng một màu, nhưng mã màu là E8590C, E8590D và e75a0c.
  - Đó là ba giá trị gõ tay; thương hiệu đổi sang màu cam khác thì ba chỗ phải sửa riêng
  - Đến chỗ thứ tư đã bị bỏ sót, vì không có gì cho biết còn chỗ nào dùng màu đó
  - Cũng trên màn hình này, chữ xám có ba mã gần giống nhau: 333333, 3A3A3A và 2f2f2f
  - Đây là file mẫu dựng sẵn với đủ tám lỗi người mới hay gặp; các lỗi khác sẽ lộ ra ở những phần sau
  > Trong file của bạn, có màu nào đang được gõ tay ở nhiều chỗ không?
- Ví dụ: có (file mẫu xấu: ba nút cam)
- Câu hỏi hay gặp: Nhìn bằng mắt thì giống nhau, sao vẫn coi là sai? Vì mắt không phân biệt được E8590C và E8590D, nhưng việc đổi màu hàng loạt thì cần biết chính xác chỗ nào dùng giá trị nào.
- 🎨 Visual hint: REAL. `assets/bad-file-sample-screen.png`, ảnh chụp màn hình file mẫu, gần như toàn khung, khoanh nhẹ ba nút cam.

---

### 09 · NUMBERED · Variables có sáu loại
- Kicker: Định nghĩa
- Title: Variables có sáu loại
- On-slide:
  - Color, number, string
  - Boolean, timing, easing
  - Tối đa 5.000 variable mỗi collection
- Speaker notes:

  > Buổi này dùng hai loại: color cho vai trò màu, và number cho spacing và cỡ chữ.

  - Figma có sáu loại: color, number, string, boolean, timing, easing
  - Number là loại hay bị quên: padding, gap, bo góc và cỡ chữ đều là number
  - Một collection chứa tối đa 5.000 variable và có thể publish thành library
  - Scope giới hạn variable chỉ hiện ở thuộc tính phù hợp, nên đặt sớm
  - Giới hạn publish theo từng gói chưa có nguồn xác nhận, nên chưa nêu con số

  > Trong token set của bạn, giá trị nào là color, giá trị nào là number?
- Ví dụ: có (token set của học viên)
- Câu hỏi hay gặp: Spacing có cần style riêng không? Không, spacing là variable kiểu number.
- 🎨 Visual hint: TYPOGRAPHIC. Sáu thẻ xếp hai hàng, mỗi thẻ một loại và một tên ví dụ.

---

### 10 · IMAGE · Panel Variables
- Kicker: Trong Figma
- Title: Panel Variables
- On-slide:
  - Collections: Colors, Radius, Sizings, Spacing, Themes
  - Groups: primary, secondary, info...
  - Alias: contrast-text trỏ về white/main
- Speaker notes:

  > Đây là panel Variables của một file design system mẫu.

  - Bên trái là các collection: Colors 128 variable, Radius 16, Sizings 220, Spacing 27, Themes 61
  - Bên dưới là các group, gom theo vai trò như primary, secondary, info, success, warning, error
  - Dòng contrast-text hiện white/main thay cho mã màu: đó là alias, đổi white/main thì mọi chỗ trỏ về nó đổi theo
  - Nhãn giao diện là của phiên bản Figma trong ảnh

  > Nếu token set của bạn có năm nhóm giá trị, bạn sẽ chia thành những collection nào?
- Ví dụ: có (ảnh chụp từ file design system mẫu của người hướng dẫn)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: REAL. Ảnh chụp panel Variables, đặt bên phải; ba dòng chú thích bên trái.

---

### 11 · DIAGRAM · Primitive và semantic
- Kicker: Cách làm
- Title: Primitive và\n*semantic*
- On-slide:
  - Primitive giữ giá trị thô: blue-500
  - Semantic giữ vai trò: color/action/fill
  - Component chỉ dùng semantic
- Speaker notes:
  > Có hai lớp tên. Lớp dưới là giá trị thô, ví dụ blue-500. Lớp trên là vai trò, ví dụ color/action/fill, và nó trỏ xuống blue-500.
  - Nút Button và liên kết Link đều dùng color/action/fill; chúng không biết blue-500 là gì
  - Khi cần chế độ tối, mode Dark của color/action/fill trỏ sang blue-300; Button và Link không phải sửa gì
  - Đường nét đứt màu cam trên sơ đồ là lỗi hay gặp: component trỏ thẳng vào primitive, nên đổi theme là phải sửa từng component
  - Đặt tên theo vai trò chứ không theo màu: color/action/fill vẫn đúng khi màu đổi, còn “blue-main” thì sai ngay lúc đổi
  - Tên dạng đường dẫn có dấu gạch chéo làm các biến tự gom nhóm trong panel
  - Buổi này chỉ làm hai collection và ba nhóm: spacing, vai trò màu và cỡ chữ; quy tắc đặt tên đầy đủ để dành cho buổi Design System
  > Token set của bạn có những vai trò màu nào, và mỗi vai trò đang trỏ về giá trị nào?
- Ví dụ: có (Button và Link cùng dùng color/action/fill)
- Câu hỏi hay gặp: Có bắt buộc hai collection không? Với file nhỏ vẫn nên làm vậy từ đầu, vì thêm lớp semantic về sau tốn công hơn nhiều so với làm ngay.
- 🎨 Visual hint: SCHEMATIC. `assets/diagrams/variable-alias-chain.html`: Button, Link, color/action/fill, blue-500, blue-300; một đường nét đứt cam từ Button thẳng tới primitive.

---

### 12 · COMPARE · Styles và variables
- Kicker: So sánh
- Title: Styles và variables
- On-slide:
  - Styles: gom nhiều thuộc tính, không alias
  - Variables: một giá trị, có alias và mode
  - Variables gắn được vào text style
- Speaker notes:

  > Hai thứ này không loại trừ nhau.

  - Styles gom nhiều thuộc tính lại thành một nhóm, như text style gồm font, cỡ chữ và line height
  - Variables là một giá trị có tên, có alias và có mode
  - Styles không alias được sang style khác, còn variables thì có, nên chuỗi primitive sang semantic chỉ làm được bằng variables
  - Variables gắn được vào text style và color style, nên hai thứ dùng chung được
  - Quy tắc của buổi: giá trị đơn thành variables; nhóm thuộc tính của chữ có thể vẫn là text style

  > Thứ nào trong file của bạn đang là style mà nên là variable?
- Ví dụ: Không cần. Slide so sánh khái niệm.
- Câu hỏi hay gặp: Có phải bỏ styles không? Không, styles vẫn dùng cho nhóm thuộc tính.
- 🎨 Visual hint: Two-column compare: Styles và Variables, mỗi bên ba dòng.

---

### 13 · IMAGE · Styles trong một file
- Kicker: Trong Figma
- Title: Styles trong một file
- On-slide:
  - Bốn nhóm style
  - Text style desktop: h1 64/80 đến caption 12/18
  - Nút cộng: Text, Color, Effect, Animation, Layout guide
- Speaker notes:

  > Ba ảnh từ cùng một file design system mẫu.

  - Panel Styles chia thành Text styles, Color styles, Effect styles và Layout guide styles
  - Nhóm Text styles desktop: h1 cỡ 64 với line height 80, h2 48 với 64, xuống đến caption 12 với 18
  - Menu dấu cộng có năm loại: Text, Color, Effect, Animation, Layout guide; tên Layout guide khớp với tên mới của layout grid
  - Cỡ chữ của text style có thể lấy từ một variable

  > File của bạn đang có những text style nào, và cỡ chữ của chúng có lấy từ variable không?
- Ví dụ: có (ba ảnh chụp từ file design system mẫu)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: REAL. Ba ảnh chụp xếp ngang, mỗi ảnh một chú thích ngắn.

---

### 14 · MILESTONE · Token set vào file
- Kicker: Activity
- Num: 15 min
- Title: Token set\n*vào file*
- Prompt: Sửa một nhóm màu trên file mẫu, rồi tạo hai collection cho token set của bạn.
- On-slide: nothing else
- Speaker notes:
  > Bốn phút đầu trên file mẫu: gắn một variable cho một trong ba nút cam và xem đổi giá trị thay đổi những gì.
  - Mười một phút còn lại trên file của bạn
  - Collection primitive nhận giá trị thô từ token set; collection semantic đặt tên theo vai trò và trỏ về primitive bằng alias
  - Ba nhóm: spacing, vai trò màu và cỡ chữ
  - Các lỗi mình sẽ chỉ ra khi làm: đặt tên theo màu, gắn component vào primitive, variable có tên nhưng chưa gắn vào layer nào
  - Modes chưa làm ở đây, để dành cho phần cuối
  > Khi xong, đổi một giá trị primitive và xem layer nào đổi theo.
- Ví dụ: Không cần. Đây là phần làm việc trên file của học viên.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Milestone layout, sienna background.

---

### 15 · SECTION DIVIDER · Auto layout
- Num: 03
- Kicker: Chuyển phần
- Title: Auto\n*layout*
- Sub: Layout co giãn theo luật, không theo đặt tay
- Speaker notes:
  > Auto layout là cách để một màn hình tự sắp lại khi nội dung hay kích thước đổi.
  - Phần hai mươi mốt phút, dài nhất sau component
  - Spacing sẽ lấy từ variables vừa tạo
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Typographic

---

### 16 · DIAGRAM · Hug, Fill, Fixed
- Kicker: Cách làm
- Title: Hug, Fill,\n*Fixed*
- On-slide:
  - Fixed: số cố định
  - Hug: ôm theo nội dung
  - Fill: lấp đầy khung cha
  - Cha Hug và con Fill: mâu thuẫn
- Speaker notes:
  > Ở file mẫu có hàng “Nhắc tôi trước 30 phút”. Cha để Hug, con để Fill, và chữ bị cắt ở “Nhắc tôi trước 3”.
  - Cha chờ con quyết định chiều rộng, còn con chờ cha; triệu chứng là chữ bị cắt chứ không phải một thông báo lỗi
  - Fixed là số cố định, Hug là ôm theo nội dung bên trong, Fill là lấp đầy phần còn lại của khung cha
  - Fill chỉ có khi khung cha là auto layout và layer con không ở chế độ Ignore auto layout (trước đây gọi là absolute position)
  - Gõ một con số vào ô width, hoặc kéo tay một layer cho vừa khít, đều làm layer đó thành Fixed
  - Một trục chỉ nên có một bên quyết định kích thước; cách sửa là cha Fixed hoặc Fill, hoặc con Hug
  - Cặp cha Hug và con Fill trong file mẫu được dựng bằng API; kết quả khi làm tay cần được thử lại
  > Trong màn hình của bạn, khung nào đang là Hug mà bên trong có con Fill?
- Ví dụ: có (file mẫu xấu: hàng "Nhắc tôi trước 30 phút")
- Câu hỏi hay gặp: Vì sao Fill không hiện trong panel? Vì khung cha chưa phải auto layout, hoặc layer con đang ở Ignore auto layout (trước đây gọi là absolute position).
- 🎨 Visual hint: SCHEMATIC. `assets/diagrams/hug-fill-fixed.html`: bốn cặp cha và con; ô cuối màu cam, chữ bị cắt.

---

### 17 · DIAGRAM · Min và max
- Kicker: Cách làm
- Title: Min và\n*max*
- On-slide:
  - Fill cần giới hạn
  - Min: không bóp quá nhỏ
  - Max: không giãn quá rộng
- Speaker notes:
  > Một nút Fill đặt trong ba khung cha rộng 192, 320 và 560. Không có giới hạn, nút co thành 160 rồi giãn thành 528.
  - Đặt min 160 và max 400 thì nút chạm min ở khung 192, lấp đầy ở khung 320, và chạm max ở khung 560
  - Min và max nằm trong ô Width và Height, bằng lệnh thêm min hoặc thêm max
  - Padding cũng đặt kích thước tối thiểu: padding 30 mỗi bên thì khung không hẹp hơn 60, và max width không ghi đè điều này
  - Padding và gap là hai con số đầu tiên nên gắn vào variables spacing vừa tạo
  - Trên màn hình nhỏ, con Fill không có min width là nguyên nhân thường gặp của chữ hay nút bị bóp
  - Từ tháng 7/2026, bản auto layout mới là mặc định cho frame mới; component cũ không tự nâng cấp
  > Con Fill nào trong màn hình của bạn cần một min width?
- Ví dụ: bản nháp (nút Fill trong ba khung cha 192, 320, 560; số liệu do chương trình đặt)
- Câu hỏi hay gặp: Bản auto layout mới có đổi cách Hug và Fill chạy không? Đang cần kiểm trong app; kết luận được ghi vào lesson trước khi dạy.
- 🎨 Visual hint: SCHEMATIC. `assets/diagrams/min-max-width.html`: ba hàng cha 192, 320, 560 với cùng một con Fill; hàng một và ba nhấn cam.

---

### 18 · IMAGE · Panel Auto layout
- Kicker: Trong Figma
- Title: Panel Auto layout
- On-slide:
  - Flow: hướng và Wrap
  - Resizing: W theo số, H Hug
  - Gap 24, Padding 40
- Speaker notes:

  > Panel Auto layout của một khung đã bật auto layout.

  - Flow là hướng sắp xếp các con, và nút mũi tên cong bên phải là Wrap
  - Resizing có hai ô: W hiện 960, H hiện 252 kèm chữ Hug; mũi tên cạnh ô W mở menu chọn Fixed, Hug, Fill và thêm min, max (ảnh chưa mở menu đó)
  - Alignment là lưới chín ô; Gap là khoảng cách giữa các con; Padding là khoảng đệm; cuối là Clip content
  - Padding và gap là hai ô nên gắn vào variables spacing

  > Khung chính trong concept của bạn hiện đặt W và H là gì?
- Ví dụ: có (ảnh chụp panel Auto layout)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: REAL. Ảnh chụp panel Auto layout bên phải; ba dòng chú thích bên trái.

---

### 19 · DIAGRAM · Wrap cho danh sách tag
- Kicker: Cách làm
- Title: Wrap cho danh sách tag
- On-slide:
  - Không Wrap: tất cả trên một hàng
  - Wrap: xuống dòng khi hết chỗ
- Speaker notes:

  > Một danh sách tag nằm trong khung hẹp: không Wrap thì khi hết chỗ các tag bị đẩy ra ngoài hoặc bị bóp.

  - Bật Wrap thì tag xuống dòng khi hết chỗ và khoảng cách giữa các tag được giữ đều
  - Nhiều người tạo nhiều hàng thủ công, rồi hỏng khi nội dung đổi
  - Cùng nhóm với Wrap là gap tự động: Between, Around, Evenly

  > Danh sách nào trong concept của bạn có số phần tử thay đổi?
- Ví dụ: bản nháp (danh sách tag trong khung hẹp)
- Câu hỏi hay gặp: Wrap khác gì tạo hai hàng? Hai hàng thủ công không tự xuống dòng khi nội dung đổi.
- 🎨 Visual hint: SCHEMATIC. Hai thẻ: khung có tag tràn và khung có tag xuống hai hàng.

---

### 20 · DIAGRAM · Ignore auto layout
- Kicker: Cách làm
- Title: Ignore auto layout
- On-slide:
  - Badge trong flow: đẩy các item khác
  - Ignore auto layout: ghim ở góc
- Speaker notes:

  > Một thẻ sản phẩm có badge Mới ở góc trên phải. Nếu badge nằm trong flow, nó đẩy các item khác.

  - Bật Ignore auto layout thì badge rời khỏi flow và được ghim theo constraint vào góc
  - Chế độ này trước đây có tên absolute position; Figma đã đổi tên
  - Theo nguồn chưa xác nhận hoàn toàn, constraint của con trong auto layout chỉ có tác dụng khi con bật Ignore auto layout; cần thử lại trong app

  > Phần tử nào trong concept của bạn nên nằm ngoài flow?
- Ví dụ: bản nháp (thẻ sản phẩm có badge Mới)
- Câu hỏi hay gặp: Khác gì padding âm? Padding âm làm lệch mọi item; Ignore auto layout giữ các item nguyên.
- 🎨 Visual hint: SCHEMATIC. Hai thẻ: danh sách bị đẩy và danh sách có badge ghim góc.

---

### 21 · COMPARE · Constraints và auto layout
- Kicker: So sánh
- Title: Constraints và auto layout
- On-slide:
  - Constraints: neo vào cạnh khung cha
  - Auto layout: sắp xếp theo luật
- Speaker notes:

  > Hai cách này giải hai bài toán khác nhau.

  - Constraints neo một phần tử vào cạnh của khung cha khi khung đổi kích thước
  - Auto layout sắp xếp các phần tử nối tiếp nhau theo luật
  - Giáo trình khác nhau về thứ tự dạy; ở buổi này auto layout đứng trước vì phần lớn màn hình là danh sách và thẻ
  - Chi tiết cần kiểm trong app: constraint không áp cho con của auto layout, trừ khi bật Ignore auto layout

  > Phần tử nào trong concept của bạn cần neo vào cạnh thay vì nối tiếp?
- Ví dụ: Không cần. Slide so sánh khái niệm.
- Câu hỏi hay gặp: Dùng cái nào trước? Danh sách và thẻ dùng auto layout; phần tử nổi dùng constraint.
- 🎨 Visual hint: Two-column compare: Constraints và Auto layout, mỗi bên ba dòng.

---

### 22 · NUMBERED · Layout guide và lưới 8
- Kicker: Cách làm
- Title: Layout guide và lưới 8
- On-slide:
  - Grid: ô vuông đều
  - Columns: cột của màn hình
  - Rows: hàng và baseline
- Speaker notes:

  > Layout grid đã được Figma đổi tên thành layout guide từ tháng 5/2025.

  - Có ba loại: grid ô vuông, columns và rows; baseline làm bằng một row guide kiểu Top
  - Layout guide chỉ là hướng dẫn nhìn, không ép layout; phần ép layout là việc của auto layout và variables
  - Thang 8 của token set là giá trị trong variables; guide giúp nhìn xem các khối có rơi theo thang đó không
  - Chi tiết cài đặt baseline cần thử trong app trước khi dạy

  > Màn hình của bạn dùng bao nhiêu cột ở kích thước hiện tại?
- Ví dụ: Không cần. Slide giới thiệu tính năng.
- Câu hỏi hay gặp: Layout guide có tự căn khối không? Không, chỉ là hướng dẫn nhìn.
- 🎨 Visual hint: TYPOGRAPHIC. Ba thẻ cùng cấp: Grid, Columns, Rows.

---

### 23 · DIAGRAM · Dựng một settings row
- Kicker: Ví dụ
- Title: Dựng một settings row
- On-slide:
  - Layer: ngang, Label Fill, Control Hug
  - Property: boolean, instance swap, variant
- Speaker notes:

  > Một dòng cài đặt có nhãn bên trái và công tắc hoặc mũi tên bên phải.

  - Dòng ngoài cùng là auto layout ngang với gap Between
  - Label là auto layout dọc và để Fill, nên dù chữ dài thì Control luôn nằm bên phải; Control để Hug
  - Property: Description là boolean, Control là instance swap, State là variant Default, Hover, Disabled
  - Padding và màu lấy từ variables; ví dụ này là bản nháp do chương trình đề xuất

  > Dòng nào trong concept của bạn có nhãn bên trái và điều khiển bên phải?
- Ví dụ: bản nháp (settings row)
- Câu hỏi hay gặp: Vì sao Label Fill? Để Control không bị đẩy xuống khi chữ dài.
- 🎨 Visual hint: SCHEMATIC. Hai thẻ: cấu trúc layer và property cùng variable.

---

### 24 · MILESTONE · Dựng bằng auto layout
- Kicker: Activity
- Num: 21 min
- Title: Dựng bằng\n*auto layout*
- Prompt: Sửa hàng cha Hug và con Fill trên file mẫu, rồi dựng màn hình concept của bạn bằng auto layout.
- On-slide: nothing else
- Speaker notes:
  > Năm phút đầu trên file mẫu: sửa hàng “Nhắc tôi trước 30 phút” và đổi một group thành frame auto layout.
  - Mười sáu phút còn lại, dựng màn hình concept của bạn: Hug cho nút và chip, Fill cho khối nội dung, min và max cho con Fill cần giới hạn
  - Padding và gap gắn vào variables spacing
  - Các lỗi mình sẽ chỉ ra: cha Hug với con Fill, gõ số vào width làm layer thành Fixed, phần tử vẫn đặt tay bằng x và y
  - Concept của bạn là màn hình đầu tiên bạn có sau phần information architecture, nên cứ dựng đủ để chạy được, chưa cần đẹp
  > Khi xong, kéo rộng và thu hẹp khung ngoài cùng để xem cái gì vỡ.
- Ví dụ: Không cần. Đây là phần làm việc trên file của học viên.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Milestone layout, sienna background.

---

### 25 · SECTION DIVIDER · Components
- Num: 04
- Kicker: Chuyển phần
- Title: *Components*
- Sub: Dựng một lần, dùng nhiều chỗ
- Speaker notes:
  > Phần dài nhất của buổi: hai mươi bốn phút.
  - Component dùng lại màn hình đã dựng ở phần trước
  - Nếu quá giờ thì rút còn hai component
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Typographic

---

### 26 · NUMBERED · What is main component · Main component là gì?
- Kicker: Định nghĩa
- Title: Main component là gì?
- On-slide:
  - What: bản gốc của một component
  - Why: sửa một lần, mọi instance đổi theo
  - When: phần tử xuất hiện từ hai lần
- Speaker notes:

  > Ở file mẫu có component Button không ai dùng và một nút đã detach. Đó là hai nửa của cùng một vấn đề.

  - Main component là bản gốc; các bản dùng ở khắp file là instance, mỗi instance nối với bản gốc của nó
  - Sửa bản gốc thì mọi instance đổi theo; bản gốc nên nằm ở một chỗ cố định, là page Components
  - Một phần tử đáng thành component khi nó xuất hiện từ hai lần trở lên, hoặc khi sắp bị chép
  - Biểu tượng của bản gốc và instance trong layers panel cần xem trong app

  > Phần tử nào trong concept của bạn xuất hiện từ hai lần trở lên?
- Ví dụ: có (file mẫu xấu: component Button không ai dùng)
- Câu hỏi hay gặp: Phần tử dùng một lần có cần component không? Thường chưa cần.
- 🎨 Visual hint: TYPOGRAPHIC. Ba thẻ What, Why, When, mỗi thẻ một ý.

---

### 27 · IMAGE · Một bản gốc, nhiều instance
- Kicker: Trong Figma
- Title: Một bản gốc, nhiều instance
- On-slide:
  - Main component: Button
  - Instance: Save, Cancel, Submit
  - Override: mỗi instance chỉ đổi chữ
- Speaker notes:

  > Bên trái là main component tên Button, bên phải là ba instance: Save, Cancel và Submit.

  - Ba nút cùng màu, cùng bo góc, cùng kích thước vì đều nối với một bản gốc
  - Chữ khác nhau là override ở từng instance; phần còn lại vẫn đi theo bản gốc
  - Nếu chữ hay đổi, nên làm thành text property

  > Nếu đổi màu nút này bây giờ, bạn phải sửa ở bao nhiêu chỗ?
- Ví dụ: có (ảnh Main và Instance)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: REAL. Ảnh Main và Instance bên phải; ba dòng chú thích bên trái.

---

### 28 · DIAGRAM · Component set và property
- Kicker: Cách làm
- Title: Component set và\n*property*
- On-slide:
  - Variant: chọn một biến thể
  - Boolean: ẩn hoặc hiện
  - Text: nội dung chữ
  - Instance swap: đổi component bên trong
- Speaker notes:
  > Ở file mẫu có bốn nút: Button, Button 2, Button copy và Button final. Bo góc là 8, 10, 12 và 9, padding mỗi nút một khác.
  - Đổi bo góc của nút chính nghĩa là sửa bốn chỗ và đoán xem chỗ nào còn sót
  - Một component set gom các biến thể của cùng một nút; sửa bản gốc thì mọi instance đổi theo
  - Bốn loại property dạy hôm nay: Variant chọn một biến thể (Size), Boolean ẩn hoặc hiện một layer (Has icon), Text là nội dung chữ (Label), Instance swap đổi một component lồng bên trong (Icon)
  - Figma có thêm loại thứ năm là Slot; buổi này chưa dùng
  - Quyết định property trước rồi mới tạo variant, vì thêm property sau khi đã có nhiều variant thường phải làm lại
  - Component dùng variables semantic, nên đổi theme là component đổi theo
  > Phần tử nào trong concept của bạn xuất hiện từ hai lần trở lên?
- Ví dụ: có (file mẫu xấu: bốn nút copy)
- Câu hỏi hay gặp: Khi nào dùng Boolean, khi nào dùng Variant? Boolean cho thứ chỉ có hai trạng thái ẩn và hiện; Variant khi có từ ba lựa chọn trở lên hoặc khi nhiều layer đổi cùng lúc.
- 🎨 Visual hint: SCHEMATIC. `assets/diagrams/component-set-properties.html`: component set Button (cam) và bốn node property bên dưới.

---

### 29 · IMAGE · Một button set thật
- Kicker: Trong Figma
- Title: Một button set thật
- On-slide:
  - Ba chiều: màu, kiểu nút, cỡ
  - Ba cỡ: Large, Medium, Small
  - Hàng cuối: disabled
- Speaker notes:

  > Đây là component Button trong một file design system mẫu; khung nét đứt là component set, mỗi nút là một variant.

  - Mỗi hàng là một màu, các nhóm cột là bốn kiểu nút, mỗi kiểu có ba cỡ; hàng cuối là disabled
  - Tạo từng nút riêng thì phải dựng hàng trăm bản; component set với property thì chỉ là một component
  - Buổi này chỉ cần một chiều; nhiều chiều thuộc buổi Design System

  > Nút của bạn cần những chiều nào, và chiều nào có thể để sau?
- Ví dụ: có (ảnh ma trận Button từ file mẫu)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: REAL. Ảnh ma trận Button bên phải; ba dòng chú thích bên trái.

---

### 30 · COMPARE · Instance và override
- Kicker: Cách làm
- Title: Instance và override
- On-slide:
  - Override: đổi riêng một instance
  - Reset: quay về giá trị của bản gốc
- Speaker notes:

  > Bạn sửa chữ trên một nút ở màn hình đăng ký. Bản gốc có đổi không? Không: đó là override.

  - Override là thay đổi chỉ nằm ở một instance; phần đã override không đổi theo bản gốc nữa
  - Nội dung hay đổi nên là text property, không phải sửa tay từng instance
  - Reset overrides đưa instance về giá trị của bản gốc mà vẫn giữ liên kết; detach thì cắt liên kết
  - Có nguồn trên forum Figma cho biết override đôi khi mất sau khi publish hoặc khi đổi variant của component cha; cần thử lại

  > Chỗ nào trong file của bạn đang sửa tay thay cho một property?
- Ví dụ: bản nháp (nút ở màn hình đăng ký)
- Câu hỏi hay gặp: Reset khác detach thế nào? Reset giữ liên kết, detach cắt liên kết.
- 🎨 Visual hint: Two-column compare: Override và Reset, mỗi bên ba dòng.

---

### 31 · NUMBERED · Sửa một lần, đổi mọi nơi
- Kicker: Cách làm
- Title: Sửa một lần, đổi mọi nơi
- On-slide:
  - 01 Mở bản gốc
  - 02 Sửa một lần
  - 03 Instance đổi theo
- Speaker notes:

  > Ở file mẫu, đổi bo góc của nút chính nghĩa là sửa bốn chỗ. Với một main component, chỉ có ba bước.

  - Chọn một instance và dùng Go to main component để mở bản gốc
  - Sửa một lần trên bản gốc, ví dụ bo góc, padding hoặc thêm một variant
  - Mọi instance còn liên kết đổi theo, trừ những phần đã bị override
  - Detach là con đường ngược lại: instance mất liên kết và việc nối lại không dễ
  - Tên lệnh và vị trí trong menu cần xem trong app trước buổi dạy

  > Nếu đổi bo góc của nút chính bây giờ, file của bạn phải sửa bao nhiêu chỗ?
- Ví dụ: có (file mẫu xấu: bốn nút với bo góc 8, 10, 12, 9)
- Câu hỏi hay gặp: Detach hoàn tác được không? Không dễ; nên tránh.
- 🎨 Visual hint: TYPOGRAPHIC. Ba thẻ đánh số 01, 02, 03.

---

### 32 · COMPARE · Nút copy và component
- Kicker: So sánh
- Title: Nút copy và\n*component*
- On-slide:
  - Cách quen tay: chép nút ra rồi sửa
  - Button, Button 2, Button copy
  - Detach để sửa nhanh
  - Sửa tay từng instance
  - Cách nên làm: một component, nhiều variant
  - Một component set cho mọi nút
  - Instance giữ liên kết với bản gốc
  - Text property cho nội dung hay đổi
- Speaker notes:
  > Bên trái là cách quen tay: chép nút ra rồi sửa. Bên phải là một component với variant và property.
  - Chép nút thì mỗi bản bắt đầu lệch một chút, rồi lệch dần
  - Detach instance để sửa nhanh làm instance mất liên kết với bản gốc, nên không còn nhận cập nhật
  - Nội dung hay đổi, như chữ trên nút, nên làm thành text property thay vì sửa tay từng instance
  - Hai nút cam trong file mẫu nhìn giống hệt nhau, nhưng một nút là instance còn nút kia đã detach; chỉ khi đổi component gốc mới thấy khác biệt
  - Có nguồn trên forum Figma cho biết đặt tên variant là Yes và No có thể làm Figma đổi thành boolean và việc gắn variable không chạy; cần thử lại trong app trước khi coi là chắc chắn
  > Trong file của bạn có phần tử nào đang là bản chép không?
- Ví dụ: có (file mẫu xấu: nút copy và instance đã detach)
- Câu hỏi hay gặp: Có bao giờ nên detach không? Khi cần một bản dùng một lần, khác hẳn component gốc; nhưng thường tạo thêm một variant thì tốt hơn.
- 🎨 Visual hint: Two-column compare, hairline borders.

---

### 33 · NUMBERED · Nested instance và slot
- Kicker: Cách làm
- Title: Nested instance và slot
- On-slide:
  - Nested: đưa property của con lên cha
  - Slot: chỗ trống cho nội dung
  - Preferred: gợi ý instance
- Speaker notes:

  > Một thẻ có nút bên trong. Nút là một instance lồng trong component thẻ.

  - Muốn đổi chữ của nút từ thẻ, dùng Expose properties from, phần Nested instances
  - Slot là một chỗ trống trong component để thả nội dung tùy ý; có trên mọi gói, Cmd hoặc Ctrl + Shift + S để chuyển layer thành slot
  - Preferred instances là danh sách component gợi ý cho chỗ đó
  - Slot là loại property thứ năm; buổi này chỉ giới thiệu

  > Component nào của bạn có phần bên trong thay đổi theo từng chỗ dùng?
- Ví dụ: bản nháp (thẻ có nút bên trong)
- Câu hỏi hay gặp: Slot khác instance swap thế nào? Instance swap đổi một thứ cố định; slot cho thả nội dung tùy ý.
- 🎨 Visual hint: TYPOGRAPHIC. Ba thẻ cùng cấp: Nested, Slot, Preferred.

---

### 34 · IMAGE · Property của TextField
- Kicker: Trong Figma
- Title: Property của TextField
- On-slide:
  - Variant, Size, State
  - Boolean: Value, Label, Help Text, Adornment
  - Nested: helper text có State và Icon riêng
- Speaker notes:

  > Một component TextField được chọn trên canvas; panel bên phải liệt kê property của nó.

  - Ba property variant: Variant (Outlined), Size (M), State (Hovered)
  - Các công tắc boolean ẩn hoặc hiện một layer: Value, Label, Help Text bật; Start Adornment, End Adornment, Select Arrow tắt
  - Helper text là instance lồng bên trong, property của nó (State, Icon) được đưa lên panel của cha bằng Expose properties from

  > Component nào của bạn có phần bên trong cần đổi từ bên ngoài?
- Ví dụ: có (ảnh TextField và panel property)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: REAL. Ảnh canvas và panel property bên phải; ba dòng chú thích bên trái.

---

### 35 · DIAGRAM · Dựng một button set
- Kicker: Ví dụ
- Title: Dựng một button set
- On-slide:
  - Variant: Style, Size, State
  - Property: Label, Has icon
  - Variable: color/action/fill
- Speaker notes:

  > Một bộ nút thường có nhiều chiều: kiểu, cỡ và trạng thái.

  - Style: Primary, Secondary, Ghost; Size: S, M, L; State: Default, Hover, Pressed, Disabled
  - Hover là một variant state của cùng một nút, không phải một component riêng
  - Label là text property, Has icon là boolean; màu lấy từ variables semantic
  - Với buổi này chỉ cần một chiều; nhiều chiều hơn thuộc buổi Design System

  > Nút của bạn có những trạng thái nào mà bạn chưa vẽ?
- Ví dụ: bản nháp (button set)
- Câu hỏi hay gặp: Có phải làm hết 24 tổ hợp không? Không, buổi này chỉ cần một chiều.
- 🎨 Visual hint: SCHEMATIC. Hai thẻ: variant và property cùng variable.

---

### 36 · NUMBERED · Ba phím tắt đáng nhớ
- Kicker: Tham khảo
- Title: Ba phím tắt đáng nhớ
- On-slide:
  - Shift A: thêm auto layout
  - Option K: tạo component
  - Cmd D: nhân bản variant
- Speaker notes:

  > Ba phím tắt gắn thẳng với ba nhiệm vụ của buổi.

  - Shift A thêm auto layout cho các layer đang chọn
  - Option K, hoặc Ctrl Alt K trên Windows, tạo component; Cmd D, hoặc Ctrl D trên Windows, nhân bản một variant
  - Đổi tên layer không có phím riêng, dùng bấm đúp; phím Detach chưa có nguồn chính thức nên không đưa lên slide

  > Việc nào bạn đang làm bằng chuột mà có thể dùng phím?
- Ví dụ: Không cần. Slide tham khảo.
- Câu hỏi hay gặp: Có phím đổi tên layer không? Không có phím riêng, dùng bấm đúp.
- 🎨 Visual hint: TYPOGRAPHIC. Ba thẻ cùng cấp, mỗi thẻ một phím lớn.

---

### 37 · MILESTONE · Biến thành component
- Kicker: Activity
- Num: 24 min
- Title: Biến thành\n*component*
- Prompt: Quyết định property trước, rồi biến hai đến ba phần tử lặp lại của concept thành component.
- On-slide: nothing else
- Speaker notes:
  > Chọn hai đến ba phần tử lặp lại: ví dụ nút, thẻ hay thanh điều hướng.
  - Viết ra property trước khi tạo variant: Size, Has icon, Label, Icon
  - Tạo component, thêm variant và component property, rồi thay các bản cũ bằng instance
  - Phần mở đầu trên file mẫu: thay bốn nút copy bằng instance của một component duy nhất
  - Các lỗi mình sẽ chỉ ra: detach để sửa nhanh, tạo property sau khi đã tạo variant, sửa tay nội dung từng instance, component dùng giá trị gõ tay
  - Quá giờ thì giữ hai component
  > Component nào của bạn có hai trạng thái trở lên?
- Ví dụ: Không cần. Đây là phần làm việc trên file của học viên.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Milestone layout, sienna background.

---

### 38 · SECTION DIVIDER · Breakpoints
- Num: 05
- Kicker: Chuyển phần
- Title: *Breakpoints*
- Sub: Một thiết kế, hai kích thước
- Speaker notes:
  > Phần cuối cho cùng một thiết kế chạy ở hai kích thước.
  - Mười bốn phút, và đây là phần chính, không cắt
  - Figma không có breakpoint tự động; mỗi breakpoint là một frame cộng một mode
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Typographic

---

### 39 · DIAGRAM · Breakpoint là một mode
- Kicker: Cách làm
- Title: Breakpoint là\n*một mode*
- On-slide:
  - Compact dưới 600dp
  - Medium 600 đến 839dp
  - Expanded 840 đến 1199dp
  - Một collection, ba mode
- Speaker notes:
  > Một designer có màn hình mobile hoàn chỉnh và được yêu cầu thêm bản desktop. Cách quen tay là nhân bản frame mobile, kéo rộng ra và sửa từng chỗ.
  - Hai tuần sau, màu nút đổi ở mobile mà desktop vẫn cũ, vì hai frame từng giống nhau chứ không còn liên quan gì
  - Figma không có media query trong chế độ thiết kế; một breakpoint là một frame có kích thước riêng cộng một mode của variables
  - Cách chia của Material Design 3: Compact dưới 600dp, Medium từ 600 đến 839dp, Expanded từ 840 đến 1199dp
  - Tạo collection Breakpoint với ba mode, rồi variable số cho thứ cần đổi theo kích thước, ví dụ padding của màn hình và cỡ chữ
  - Mỗi frame đặt mode riêng; số cột của các thẻ đổi nhờ auto layout với Fill và min width, chứ không nhờ mode
  - Gói Professional cho tối đa 10 mode mỗi collection; mode áp theo từng frame, nên một layer lồng bên trong có thể giữ mode khác
  > Màn hình của bạn cần một kích thước thứ hai nào trước tiên?
- Ví dụ: bản nháp (designer nhân bản frame mobile thành desktop; tình huống do chương trình đặt)
- Câu hỏi hay gặp: Có cần đủ ba mode không? Với hai kích thước thì hai mode là đủ; mode thứ ba có thể thêm sau.
- 🎨 Visual hint: SCHEMATIC. `assets/diagrams/breakpoints-modes.html`: ba frame (Compact một cột, Medium hai cột, Expanded ba cột) và node Breakpoint (cam) nối nét đứt tới từng frame.

---

### 40 · DIAGRAM · Một pricing card, hai kích thước
- Kicker: Ví dụ
- Title: Một pricing card, hai kích thước
- On-slide:
  - Cấu trúc: dọc, gap 16, CTA Fill
  - Property: Highlighted, Period, Plan
  - Breakpoint: ba card ngang hoặc dọc
- Speaker notes:

  > Pricing card là ví dụ tốt để nối ba phần của buổi.

  - Card là auto layout dọc với gap 16; tên gói, giá, danh sách tính năng và nút CTA để Fill
  - Highlighted là boolean thêm viền và badge, Period là text, Plan là variant Free, Pro, Team
  - Ở Expanded ba card xếp ngang, ở Compact xếp dọc nhờ auto layout với Fill và min width; mode đổi padding và cỡ chữ
  - Ví dụ này là bản nháp do chương trình đề xuất

  > Thành phần nào trong màn hình của bạn lặp theo hàng ngang mà trên màn hình nhỏ phải xếp dọc?
- Ví dụ: bản nháp (pricing card)
- Câu hỏi hay gặp: Số cột đổi nhờ mode không? Không, nhờ auto layout với Fill và min width.
- 🎨 Visual hint: SCHEMATIC. Ba thẻ cùng cấp: Cấu trúc, Property, Breakpoint.

---

### 41 · MILESTONE · Kích thước thứ hai
- Kicker: Activity
- Num: 14 min
- Title: Kích thước\n*thứ hai*
- Prompt: Tạo collection Breakpoint với các mode, rồi cho màn hình và component chạy ở kích thước thứ hai.
- On-slide: nothing else
- Speaker notes:
  > Tạo collection Breakpoint với ba mode: Compact, Medium, Expanded.
  - Tạo hai đến ba variable số, ví dụ screen/padding và type/body/size, mỗi mode một giá trị
  - Nhân bản màn hình thành frame thứ hai, đặt mode khác và điều chỉnh để component co giãn đúng
  - Các lỗi mình sẽ chỉ ra: quên đặt mode cho frame, con Fill thiếu min width, sửa hai frame riêng thay vì sửa component và variables
  - Gói không đủ mode thì dùng hai mode thay cho ba
  > Component nào của bạn co giãn đúng, và component nào chưa?
- Ví dụ: Không cần. Đây là phần làm việc trên file của học viên.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Milestone layout, sienna background.

---

### 42 · SECTION DIVIDER · Handoff
- Num: 06
- Kicker: Chuyển phần
- Title: *Handoff*
- On-slide:
  - Từ file Figma đến người dựng và người dùng
- Speaker notes:

  > Phần cuối nói về những gì xảy ra sau khi file dựng xong.

  - Dev Mode để bàn giao, một checklist trước khi gửi, và vài con số accessibility
  - Prototype có lesson riêng nên không nằm ở buổi này
  - Mô tả việc làm junior cho thấy handoff xuất hiện ở 5 trên 12 tin; mẫu nhỏ nên chỉ dùng để chọn trọng tâm
- Ví dụ: Không cần. Slide chuyển phần.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Typographic

---

### 43 · NUMBERED · What is Dev Mode · Dev Mode là gì
- Kicker: Định nghĩa
- Title: Dev Mode là gì
- On-slide:
  - Ai dùng được: từ gói Professional
  - Developer thấy: số đo, code, variable
  - Auto layout 2026: gần flexbox hơn
- Speaker notes:

  > Dev Mode là chế độ xem dành cho người dựng: developer mở file và thấy số đo, code snippet và tên variable của từng layer.

  - Gói Starter không có Dev Mode; Professional, Organization và Enterprise có; annotation cần Full seat
  - Hai trang help của Figma mâu thuẫn về việc gói Professional có đặt được Ready for dev hay không; cần kiểm trong app
  - Từ tháng 7/2026 code từ Dev Mode khớp thuộc tính flexbox hơn; Between với một con thì căn đầu, gap không âm
  - Tên variable và layer chính là những gì developer đọc

  > Nếu developer mở file của bạn bây giờ, họ đọc được gì từ tên layer?
- Ví dụ: Không cần. Slide định nghĩa.
- Câu hỏi hay gặp: Gói Starter dùng Dev Mode được không? Không.
- 🎨 Visual hint: TYPOGRAPHIC. Ba thẻ cùng cấp: Ai dùng được, Developer thấy gì, Auto layout 2026.

---

### 44 · COMPARE · Checklist trước khi bàn giao
- Kicker: Cách làm
- Title: Checklist trước khi bàn giao
- On-slide:
  - Cấu trúc: tên layer, page đã chốt, không nháp lẫn
  - Giá trị: variables, không detach, đủ trạng thái
- Speaker notes:

  > Sáu điều nên kiểm trước khi gửi file cho người dựng.

  - Ba điều về cấu trúc: layer đặt tên theo vai trò, có một chỗ cho bản đã chốt, không còn frame nháp lẫn vào
  - Ba điều về giá trị: màu và spacing từ variables, không còn instance bị detach, component có đủ trạng thái
  - Đây là bản tổng hợp từ best practices của Figma và từ lỗi của file mẫu, không phải checklist chính thức
  - Checklist của Material, Carbon, Primer, Polaris và GOV.UK chưa được nghiên cứu

  > Mục nào trong sáu mục này file của bạn chưa đạt?
- Ví dụ: có (file mẫu xấu: tám lỗi là mặt trái của checklist)
- Câu hỏi hay gặp: Checklist này có chính thức không? Không, là tổng hợp.
- 🎨 Visual hint: Two-column compare: Cấu trúc và Giá trị, mỗi bên ba dòng.

---

### 45 · NUMBERED · Ba con số cần nhớ
- Kicker: Con số
- Title: Ba con số cần nhớ
- On-slide:
  - 4,5:1 cho chữ thường
  - 3:1 cho chữ lớn
  - 24 × 24 mục tiêu chạm tối thiểu
- Speaker notes:

  > Ba con số lấy từ WCAG 2.2, và đều kiểm được ngay trong thiết kế.

  - Chữ thường cần tỉ lệ tương phản tối thiểu 4,5 trên 1 với nền; chữ lớn, từ 18pt hoặc 14pt đậm, cần 3 trên 1
  - Phép so sánh không làm tròn, nên 4,499 trên 1 là trượt
  - Mục tiêu chạm tối thiểu 24 nhân 24 pixel ở mức AA, và 44 nhân 44 ở mức AAA
  - Con số 48dp của Material và 44pt của Apple chưa xác nhận nên không đưa lên slide

  > Cặp màu chữ và nền chính trong concept của bạn đạt bao nhiêu trên 1?
- Ví dụ: có (WCAG 2.2, Understanding 1.4.3)
- Câu hỏi hay gặp: Chữ lớn là bao lớn? Từ 18pt, hoặc 14pt đậm.
- 🎨 Visual hint: TYPOGRAPHIC. Ba thẻ cùng cấp, mỗi thẻ một con số lớn.

---

### 46 · NUMBERED · Bốn câu hỏi trước khi kết
- Kicker: Kiểm tra nhanh
- Title: Bốn câu hỏi trước khi kết
- On-slide:
  - Variables: blue-500 hay color/action/fill?
  - Auto layout: cha Hug và con Fill gây ra gì?
  - Component: đổi chữ mà không detach dùng gì?
  - Breakpoint: đổi mode có đổi chiều rộng frame không?
- Speaker notes:

  > Bốn câu hỏi, mỗi phần một câu.

  - Đáp án: màu semantic color/action/fill, vì component chỉ nên dùng lớp semantic
  - Cha Hug và con Fill mâu thuẫn nên chữ bị cắt; cách sửa là cha Fixed hoặc Fill, hoặc con Hug
  - Text property, không phải detach; mode không đổi chiều rộng frame, chỉ đổi giá trị của variable
  - Bộ 40 câu đầy đủ là đề xuất của chương trình, nằm trong research của lesson

  > Câu nào trong bốn câu này bạn chưa chắc?
- Ví dụ: Không cần. Slide kiểm tra.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: TYPOGRAPHIC. Bốn thẻ cùng cấp, mỗi thẻ một câu hỏi.

---

### 47 · PRACTICE · Hoàn thiện file
- Kicker: Practice
- Title: Hoàn thiện\n*file của bạn*
- On-slide:
  - Hoàn thiện file
  - Hoàn thành phần còn dở
  - Rà màu và spacing gõ tay
  - Kiểm tra component ở hai kích thước
  - Đặt tên layer còn sót
  - Gửi lại
  - Link file Figma, quyền xem
  - Ba chỗ còn cần sửa
  - Cách sửa cho từng chỗ
  - Gửi trước buổi Design System
- Speaker notes:
  > Success check của hôm nay có ba ý: file có pages và tên layer rõ, màu và spacing lấy từ variables, và một component set chạy được ở hai kích thước.
  - Homework gồm hai việc: hoàn thiện phần còn dở của bốn nhiệm vụ trong file, và viết phần reflection
  - Reflection là ba chỗ còn giá trị gõ tay, tên layer mặc định hoặc kích thước Fixed không cần thiết, kèm cách sửa
  - File được nhận bằng link Figma với quyền xem
  - Buổi sau là Design System, nơi variables và component hôm nay được dùng lại và đặt tên theo quy tắc atomic
  > Bạn còn dở phần nào, và phần đó nằm ở nhiệm vụ mấy?
- Ví dụ: Không cần. Slide giao bài tập.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: TWO CARDS. Card 1 "Hoàn thiện file" (bốn bullet), card 2 "Gửi lại" (bốn bullet); mỗi card có icon outline.

---

### 48 · END · Viết một lần, dùng nhiều chỗ
- Kicker: Takeaway
- Title: Viết *một lần*,\ndùng nhiều chỗ
- On-slide:
  - UI Foundations: Building in Figma
- Speaker notes:
  > Variables, auto layout và component đều làm cùng một việc: viết một lần và dùng ở nhiều chỗ.
  - Cảm ơn bạn
  - File hôm nay là đầu vào của buổi Design System
  - Guide dọn file và file mẫu gửi lại sau buổi
- Ví dụ: Không cần. Slide kết.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: End layout, light paper-deeper background.
