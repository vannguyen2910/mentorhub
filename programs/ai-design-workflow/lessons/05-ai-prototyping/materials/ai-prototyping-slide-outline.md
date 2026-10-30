---
title: "AI Prototyping"
lesson_file: "ai-prototyping-lesson.md"
level: ""
slide_count: 29
duration: "90 min"
status: draft
built_deck: ""
last_synced: 2026-10-30
---

> **Source of truth:** `ai-prototyping-lesson.md`

> **Copy standard:** mọi Kicker, Title và dòng On-slide đọc được trong một cái nhìn, không câu nào quá khoảng 15 từ. Speaker notes dùng ngôi "mình".

> **Deck status:** chưa có deck nào được build từ outline này.

---

## Session metadata

| Field | Value |
|---|---|
| Program | AI Design Workflow |
| Track / session | Buổi theory tuần 5 (Lesson 5), 90 phút, online, 7 đến 8 học viên; Practice 5 ngay sau đó |
| Stage | Develop |
| Prior session | Lesson 4 và Practice 4: Explore Ideas |
| Next session | Practice 5: Build prototype main flow |
| Running example | Một delivery app hư cấu (màn hình "Chọn thời gian giao" ở activity); học viên làm trên case của chính mình ở Practice 5 |

---

## Slide structure: 29 slides

- Arc: **Open** (cover, ice breaker) → **Theory** → **Bridge** (break, cheat sheet) → **Activity** (Rule-break hunt, 5 phút) → **Hỏi đáp** → **Close** (việc tiếp theo, kết thúc).
- Theory gồm một divider và bốn phần: The Aim, One View, The Second View, Gate/Rules/Skill.

---

## Slides

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Develop
- Title: Prototype\nwith *rules*
- Subtitle: Give AI your rules, not a blank page
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: Ảnh thật từ Unsplash bàn tay đang xếp các thẻ giấy thành một khung màn hình trên bàn, ánh sáng ấm, gần gũi
- Speaker notes:
- 🎨 Visual hint: Cover layout, cố định. Panel trái trắng với dòng năm, nhãn stage, title (accent ở dòng 2) và subtitle. Panel phải là ảnh thật với gradient tối, tên và ba dòng credentials ở góc dưới trái.
---

### MILESTONE · Ice breaker
- Num: 6
- Kicker: Open
- Title: Looked fine,\n*was wrong*
- Sub: Tên bạn, và một lần AI dựng màn hình trông ổn mà hóa ra sai
- Speaker notes:

  > Lần gần nhất AI dựng cho bạn một màn hình trông ổn, đến khi kiểm lại bạn mới thấy sai. Sai ở đâu, và bạn phát hiện bằng cách nào?

  - Sáu phút, cả lớp; mình nói trước hai mươi giây, rồi mỗi người nói tên và một câu
  - Ghi nhanh các kiểu lỗi lên bảng: màu lệch, component lạ, điều hướng khác nhau, nội dung bịa
  - Hỏi nhanh về tuần 4: hướng đã chọn và flow đã có chưa
  - Ai chưa có câu chuyện thì kể điều mình sợ nhất khi AI dựng giao diện

  > **Mình giữ bảng này để quay lại ở cuối buổi.**

  > Những lỗi này nghe quen không? Mình vào phần nội dung.
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số phút lớn; bên dưới một cột trống "Kiểu lỗi" để ghi.
---

### SECTION DIVIDER · Theory
- Num: 01
- Kicker: Four parts
- Title: Give AI the\n*right context*
- Sub: The Aim, One View, The Second View, Gate/Rules/Skill
- Speaker notes:

  > Những lỗi trên bảng đều có chung một nguồn: AI không có gì cố định để bám vào.

  - Bốn phần, mỗi phần kết thúc bằng một câu hỏi ngắn bỏ phiếu bằng chat
  - Activity năm phút nằm sau phần cuối; việc dựng prototype là ở buổi practice
  - Phần nặng nhất là One View: nó đặt tên cho những gì bạn sẽ đưa cho AI

  > Mình bắt đầu từ câu hỏi: vì sao dựng từng màn hình lại bị lệch?
- 🎨 Visual hint: TYPOGRAPHIC. Nền paper-deeper, số phần lớn, accent ở dòng 2.
---

### COMPARE · Four problems
- Kicker: So sánh
- Title: Bốn vấn đề, một cách sửa
- On-slide:
  - Mọi thứ lệch dần: mọi màn dùng chung bố cục
  - AI quên hết: một pattern viết sẵn, đọc lại mỗi prompt
  - Trạng thái bị quên: ghi đủ trạng thái ngay từ đầu
  - Làm lại tốn token: ít phải suy lại, ít phải thử lại
- Ví dụ: có (delivery app: ba màn Giỏ hàng, Chọn thời gian giao, Thanh toán dựng ở ba lần prompt riêng)
- Câu hỏi hay gặp:
  - Viết prompt thật hay có đủ không? Prompt giúp từng màn, nhưng không giữ được những thứ phải cố định giữa các màn.
  - Có số đo chi phí token không? Deck gốc của lesson 1 có số liệu; buổi này không dùng vì chưa kiểm.
- Speaker notes:

  > Giả sử bạn dựng ba màn của một delivery app: giỏ hàng, chọn thời gian giao, thanh toán, mỗi màn một prompt riêng. Màn một và màn hai thường ổn. Màn ba có thể đã đổi thanh điều hướng và màu nút.

  - Vấn đề một: mọi thứ lệch dần, nút ở màn một hơi khác nút ở màn ba; cách sửa là mọi màn dùng chung bố cục
  - Vấn đề hai: AI quên hết, mỗi yêu cầu bắt đầu lại từ đầu; cách sửa là một pattern viết sẵn, đọc lại ở mỗi prompt
  - Vấn đề ba: trạng thái rỗng, đang tải, lỗi bị quên đến khi người dùng gặp; component inventory ghi mọi trạng thái từ đầu
  - Vấn đề bốn: mỗi lần prompt lại, AI xử lý lại phần đi trước, nên làm lại tốn thời gian và tiền; ít phải suy lại thì ít phải thử lại
  - Vấn đề hai và bốn cùng một gốc: AI không có context cố định, nên cùng một cách sửa giải quyết cả hai
  - Đây là quan sát từ thực hành của chương trình, không phải kết quả đo

  > **Cả bốn vấn đề quy về một gốc: AI không có gì cố định để bám.**

  > Bạn đã thấy ba màn của một app có ba kiểu điều hướng chưa?
- 🎨 Visual hint: SCHEMATIC. Bốn hàng, mỗi hàng một vấn đề bên trái và cách sửa bên phải, nối bằng mũi tên. Hàng AI quên hết và hàng làm lại tốn token cùng chỉ về một gốc "không có context cố định".
---

### DIAGRAM · The Aim
- Kicker: Mục tiêu
- Title: Ba ý của The Aim
- On-slide:
  - Systematic prototype mindset: hệ thống trước, màn hình sau
  - Pattern first: Design Pattern là đầu vào của prototype
  - AI-assisted, không phải AI-generated
- Ví dụ: có (delivery app: định nghĩa hệ thống một lần, rồi dựng ba màn từ nó)
- Câu hỏi hay gặp:
  - Pattern ở đây là gì? Design Pattern là tên chung cho bộ token, component, template và shell.
  - Vì sao AI-assisted? Học viên giữ các quyết định: định nghĩa hệ thống, đặt ràng buộc, review từng màn.
- Speaker notes:

  > Với delivery app, thay vì dựng màn giỏ hàng rồi màn thanh toán từ đầu, bạn định nghĩa hệ thống một lần. Ba màn sau đó là ba cách sắp xếp những thứ đã có.

  - Ý một: tư duy hệ thống. Hệ thống đi trước, màn hình đi sau
  - Ý hai: pattern first. Design system là đầu vào của prototype, không phải đầu ra của việc thiết kế
  - Ý ba: AI lắp ráp, còn bạn định nghĩa hệ thống, đặt ràng buộc và review từng màn
  - Nielsen Norman Group (2025) có một nghiên cứu, được dẫn trong lesson AI Prototype Development: công cụ làm theo chỉ dẫn chung nhưng thiếu độ tinh tế. Mình chưa mở bản gốc
  - Cách nghĩ của lập trình: định nghĩa một mẫu một lần, dùng lại nhiều lần và chỉ tuỳ chỉnh phần khác biệt

  > **Hệ thống là đầu vào của prototype, không phải đầu ra.**

  > Trong ba ý này, ý nào khác nhất với cách bạn đang làm?
- 🎨 Visual hint: SCHEMATIC. Ba khối ngang: mindset, pattern first, AI-assisted; một mũi tên từ hệ thống sang ba màn hình.
---

### NUMBERED · Big teams
- Kicker: Ví dụ
- Title: Đội lớn làm thế nào
- On-slide:
  - Stripe cho AI đọc rules file, khung điều hướng và design system qua MCP
  - Atlassian cài skill vào repo, kèm chỉ dẫn ngắn trong AGENTS.md
  - Vercel đóng gói component và block trong registry cho AI đọc
  - Uber: agent đọc design system, spec ba nền tảng dưới 2 phút (số của Uber)
- Ví dụ: có (bốn đội công khai: Stripe [1][2], Atlassian [3], Vercel [8], Uber [9]; Stripe `[to confirm]`)
- Câu hỏi hay gặp:
  - Có số đo hiệu quả không? Chỉ có số của chính Uber và lời nói của người xây công cụ ở Stripe, không có nghiên cứu độc lập.
  - Cần MCP mới làm được không? Không; hôm nay chỉ cần rules file và design system.
- Speaker notes:

  > Ở Stripe, một designer xây công cụ để designer và PM tạo prototype từ design system, thay vì từ trang trắng. Người xây nói công cụ làm được khoảng 80%, designer vẫn là người lái.

  - Bốn đội, bốn cách đóng gói, nhưng cùng một ý: đưa design system vào dạng AI đọc được trước
  - Atlassian có bộ skill chỉ cho nhân viên, còn CLI và MCP server công khai
  - Vercel nói qua blog, không nêu số liệu hay khách hàng
  - Số của Uber là số của chính Uber, không có số đo độ chính xác
  - Phần lớn nguồn là tài liệu của vendor hoặc lời kể của một người; chưa có nghiên cứu độc lập

  > **Mình nêu số liệu kèm nguồn, và nói thẳng khi chưa có số đo.**

  > Câu hỏi 30 giây: màn ba có thanh điều hướng khác màn một. Nguyên nhân nhiều khả năng nhất? A, prompt chưa đủ hay. B, AI không có gì cố định để bám. Gõ A hoặc B vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Numbered lưới 2 cột, bốn ô; tên công ty chữ lớn, một dòng mô tả bên dưới.
---

### DIAGRAM · One View
- Kicker: Nền chuẩn
- Title: One View là gì?
- On-slide:
  - Mọi prototype dùng chung một starter và một cấu trúc folder
  - Cùng component và cùng content voice
  - Bên trong có bốn layer và một journey chính
  - Trong deck gốc: trang design-system.html
- Ví dụ: có (delivery app: nhãn "Đơn hàng" ở mọi màn, không lúc "Đơn" lúc "Order")
- Câu hỏi hay gặp:
  - View là gì? Một cách nhìn vào cùng một product. One View là nền chuẩn; The Second View là prototype thật.
  - Content voice là gì? Cách đặt nhãn, thông báo và thuật ngữ nhất quán giữa các màn.
  - One View nhìn thấy ở đâu? Trang design-system.html: gom token, component, template và shell để kiểm tra hệ thống trước khi dựng màn.
- Speaker notes:

  > Mở một delivery app và nhìn từng màn: chỗ này ghi "Đơn hàng", chỗ kia ghi "Order", chỗ nọ chỉ ghi "Đơn". Content voice đổi giữa các màn cũng là một kiểu lệch.

  - One View là nền chuẩn mà mọi prototype xuất phát từ nó
  - Bốn thứ giống nhau ở mọi prototype: starter, cấu trúc folder, component và content voice
  - Content voice là cách đặt nhãn, thông báo và thuật ngữ; nó nằm trong rules file ở phần sau
  - Bên trong One View có bốn layer và một journey chính; hai slide kế nói từng thứ
  - "View" là một cách nhìn vào cùng một product; slide The Second View nói cách nhìn còn lại
  - Trong các deck của khoá AI Prototype Development, One View là trang design-system.html, nơi kiểm tra hệ thống trước khi dựng màn

  > **Cùng một nền thì mọi prototype có cùng content voice.**

  > Product của bạn hiện có bao nhiêu cách gọi cho cùng một thứ?
- 🎨 Visual hint: SCHEMATIC. Một khối lớn "One View" chứa bốn ô: starter, folder, component, content voice; bên trong ghi "bốn layer + một journey".
---

### DIAGRAM · The Design Stack
- Kicker: Bản đồ
- Title: Bốn layer của Design Pattern
- On-slide:
  - Template: bố cục một loại trang
  - Shell: khung lặp ở mọi màn hình
  - Component: nút, ô nhập, thẻ chọn
  - Token: màu, cỡ chữ, khoảng cách
  - Cả bộ bốn layer gọi là Design Pattern
  - Design system của bạn có token và component; shell và template là của product
- Ví dụ: có (delivery app: màu chính là token, nút là component, header và menu là shell, trang danh sách là template)
- Câu hỏi hay gặp:
  - Pattern là nhóm component như bộ lọc? Không; ở đây Design Pattern là tên chung cho cả bộ. Nhóm component như bộ lọc gọi là "nhóm component".
  - Vì sao thứ tự này? Layer thấp ít đổi và nhiều thứ phụ thuộc; cố định trước. Đây là suy luận, chưa có nghiên cứu đo.
  - Các hệ thống khác gọi thế nào? Carbon gọi UI shell, Material gọi layout scaffold, Polaris tách template và composition. Không có chuẩn ngành, nên lớp dùng bộ từ này.
- Speaker notes:

  > Mở một delivery app trên điện thoại. Màu xanh của nút là token. Nút là component. Thanh trên cùng và menu dưới là shell. Trang danh sách nhà hàng là template.

  - Bốn layer xếp từ dưới lên: token, component, shell, template
  - Cả bộ gọi là Design Pattern, đúng cách chương trình đã dùng ở khoá AI Prototype Development
  - Design system của bạn có token và component; chưa có shell và template
  - Shell và template thuộc về từng product, nên bạn tự định nghĩa cho product của bạn
  - Thứ tự từ dưới lên là suy luận từ cấu trúc: đổi shell là đổi mọi màn hình
  - Khi đọc tài liệu khác, đối chiếu từ của họ với bốn layer này: Carbon nói UI shell, Material nói layout scaffold (nguồn 4 và 6)

  > **Bốn layer này là thứ bạn đưa cho AI trước khi nó dựng.**

  > Trong design system của bạn hôm nay, layer nào đang thiếu?
- 🎨 Visual hint: SCHEMATIC. Diagram `design-stack.html`: bốn khối xếp chồng, template trên cùng, token dưới cùng; một ngoặc bên phải ghi "Design Pattern".
---

### DIAGRAM · Shell
- Kicker: Định nghĩa
- Title: Shell là gì?
- On-slide:
  - Khung lặp ở mọi màn hình, còn gọi shared layout
  - Header, menu, vùng nội dung
  - Năm quyết định: header, side nav, mục điều hướng, nút chính, màn hình hẹp
- Ví dụ: có (delivery app: header có tên app, menu Trang chủ, Đơn hàng, Cài đặt, thu thành menu ở màn hình hẹp)
- Câu hỏi hay gặp:
  - Shell có phải một component? Là một nhóm component đặt cố định; Carbon gọi là UI shell và tách thành header và panel.
  - Product nhỏ có cần không? Có; ít nhất là quyết định có điều hướng hay không.
- Speaker notes:

  > Màn giỏ hàng và màn thanh toán của delivery app có cùng một thanh trên cùng và cùng một menu. Phần lặp đó là shell.

  - Shell là khung bao mọi màn hình; bạn quyết định nó một lần
  - Năm quyết định: có header không, có side nav không, các mục điều hướng, nút chính ở đâu, màn hình hẹp thì sao
  - Đây là thứ AI hay tự thêm hoặc đổi từng màn nếu bạn không cố định
  - Năm quyết định này là phần bạn tự định nghĩa cho product của bạn

  > **Quyết định shell một lần, rồi cấm AI tự thêm điều hướng.**

  > Product của bạn hiện có mấy kiểu điều hướng khác nhau?
- 🎨 Visual hint: REAL. Ảnh `library/lessons/03-develop/ai-prototype-development/assets/lesson-5-showcase-wireframe-3-plan.png` (dự án demo của khoá, ghi chú nhỏ "Dự án demo: Travel Buddy"). Khoanh thanh tab dưới (Discover / Plan / Connect / Journal) và nhãn "Shell"; vùng còn lại ghi "Nội dung từng màn". Nếu cần, thêm `wireframe-4-connect.png` để thấy cùng thanh tab ở màn khác.
---

### DIAGRAM · Template
- Kicker: Định nghĩa
- Title: Template là gì?
- On-slide:
  - Bố cục một loại trang, chưa có nội dung cuối
  - Ví dụ: trang danh sách, trang chi tiết, trang cài đặt
  - Mỗi template có các vùng: chính, phụ, thanh hành động
- Ví dụ: có (delivery app: danh sách nhà hàng, chi tiết món, thanh toán)
- Câu hỏi hay gặp:
  - Cần bao nhiêu template? Hai đến ba cho một flow; nhiều hơn thường là chưa chọn.
  - Template khác trang? Template là khung chưa có nội dung; trang là template đã điền nội dung thật.
- Speaker notes:

  > Trang danh sách nhà hàng và trang danh sách đơn hàng của delivery app khác nội dung nhưng cùng một bố cục: tiêu đề, bộ lọc, danh sách thẻ. Bố cục đó là template.

  - Template trả lời câu hỏi nội dung nằm ở đâu trong khung của shell
  - Hai đến ba template là đủ cho một flow
  - Frost mô tả template là bộ khung cấp trang; nội dung thật làm lộ chỗ hệ thống chưa chịu được
  - Việc chọn template cho flow là phần bạn tự định nghĩa cho product của bạn

  > **Một màn hình, một template. Không có template phù hợp thì AI phải dừng và hỏi.**

  > Flow của bạn dùng mấy kiểu trang?
- 🎨 Visual hint: REAL. Ba ảnh cạnh nhau từ `library/lessons/03-develop/ai-prototype-development/assets/`: `wireframe-2-discover.png` (danh sách, chi tiết) và `wireframe-3-plan.png` (danh sách, bản đồ); ghi chú nhỏ "Dự án demo: Travel Buddy". Tô và đặt tên các vùng của từng template. `wireframe-1-onboarding.png` dùng dự phòng.
---

### DIAGRAM · One journey
- Kicker: Phạm vi
- Title: Một đường đến thành công
- On-slide:
  - Một shell, một journey
  - Từ lúc bắt đầu đến lúc đạt mục tiêu
  - Không phải cả product
- Ví dụ: có (delivery app: từ mở app đến đặt xong một đơn, năm màn)
- Câu hỏi hay gặp:
  - Một journey có đủ để test không? Đủ để test đường chính, không đại diện cho cả product.
  - Journey thứ hai thì sao? Theo lesson Scaling the Prototype của chương trình, nó tốn ít công hơn vì hệ thống đã có; chưa có số đo.
- Speaker notes:

  > Với delivery app, đường chính là: mở app, chọn món, chọn thời gian giao, thanh toán, đặt xong. Năm màn, một đường từ đầu đến thành công.

  - Phạm vi của buổi practice là một shell và một journey, không phải cả product
  - Journey là đường chính từ lúc người dùng bắt đầu đến lúc đạt mục tiêu
  - Một journey là một mảnh của product, nên prototype này để test đường chính
  - Journey thứ hai thường tốn ít công hơn vì hệ thống đã có; đây là quan sát của chương trình, chưa có số đo
  - Flow đến từ tuần 4, không phải AI nghĩ ra

  > **Một shell và một journey. Chưa phải cả product.**

  > Đường chính của product bạn gồm mấy màn?
- 🎨 Visual hint: REAL. Ảnh `library/lessons/03-develop/ai-prototype-development/assets/lesson-5-showcase-user-flow-swimlane.webp` (dự án demo: Travel Buddy), đánh dấu một đường từ "Bắt đầu" đến "Thành công". Nếu swimlane quá nhiều làn, cắt về làn Traveler.
---

### IMAGE · Same screen, two prompts
- Kicker: Demo
- Title: Một màn, hai prompt
- On-slide: Trái: prompt mơ hồ. Phải: prompt kèm rules file.
- Ví dụ: bản nháp (màn "Chọn thời gian giao" của delivery app, hai kết quả dựng sẵn trước buổi dạy `[to confirm]`)
- Câu hỏi hay gặp:
  - Vì sao không chạy trực tiếp? Chờ AI chạy mất thời gian và kết quả khó đoán, nên hai bản được dựng sẵn để chắc đủ giờ.
  - Hai bản có thật không? Có; nhưng đây là một ví dụ, không phải số đo mức AI vi phạm quy tắc.
- Speaker notes:

  > Cùng một màn hình, cùng một AI. Bên trái prompt chỉ nói "dựng màn chọn thời gian giao". Bên phải kèm rules file. Trước khi mình mở file, bạn đoán bản nào dùng đúng design system.

  - Cho cả lớp đoán trước, rồi bỏ phiếu bằng chat
  - Mở file bản trái: màu thô, điều hướng riêng, component lạ
  - Mở file bản phải: dùng đúng token và component, nằm trong shell
  - Hai bản dựng sẵn trước buổi dạy; không chạy trực tiếp
  - Đây là một ví dụ, không phải số đo mức AI vi phạm quy tắc

  > **Khác biệt không nằm ở prompt hay hơn, mà ở thứ AI được đưa vào trước.**

  > Câu hỏi 30 giây: AI thêm một thanh điều hướng riêng ở màn ba. Layer nào bị vi phạm? A, component. B, shell. Gõ A hoặc B vào chat.
- 🎨 Visual hint: REAL. Hai ảnh chụp màn hình đặt cạnh nhau (bản mơ hồ và bản có rules file) `[to confirm]`: cần dựng trước buổi dạy.
---

### DIAGRAM · The Second View
- Kicker: Prototype thật
- Title: The Second View
- On-slide:
  - Prototype thật, dựng từ One View
  - Sửa ở One View, rồi để quy tắc đưa thay đổi sang
  - Chỉ layer token tự động cập nhật
  - Phần còn lại là một prompt có quy tắc
- Ví dụ: có (delivery app: đổi màu chính ở token thì nút ở cả năm màn đổi theo; đổi tên menu ở shell thì phải dựng lại qua một prompt)
- Câu hỏi hay gặp:
  - Đổi ở One View là mọi thứ tự cập nhật? Chỉ layer token. Với component, shell và template, thay đổi được đưa sang qua một prompt có kiểm soát, theo quy tắc.
  - Có sửa trực tiếp ở prototype được không? Được, nhưng sửa ở nguồn trước thì lỗi không quay lại.
- Speaker notes:

  > Bạn đổi màu chính trong token: nút ở cả năm màn đổi theo. Bạn đổi tên một mục menu trong shell: AI không tự biết, bạn phải dựng lại qua một prompt có quy tắc.

  - The Second View là prototype thật: chạy được trong trình duyệt, dựng từ One View
  - One View cho biết "đúng" trông thế nào; The Second View là nơi áp dụng vào flow của bạn
  - Thay đổi được đưa từ One View sang The Second View theo quy tắc đã viết
  - Chỉ layer token tự cập nhật, như lesson Scaling the Prototype của chương trình đã nói
  - Quy tắc: sửa ở nguồn, dựng lại phần bị ảnh hưởng, rồi review
  - Trang design-system.html và các màn hình cùng dùng tokens.css, nên đổi token là cả hai đổi theo
  - Nhiều demo nói "tự động cập nhật" mà không nói rõ lớp nào; đó là chỗ cần nói thẳng
  - Hệ thống của bạn cập nhật đáng tin cậy, và điều đó hữu ích hơn là tự động

  > **Sửa ở One View, rồi để quy tắc đưa thay đổi sang The Second View.**

  > Trong prototype của bạn, thay đổi nào sẽ phải qua một prompt thay vì tự cập nhật?
- 🎨 Visual hint: SCHEMATIC. Hai khối cạnh nhau, One View và The Second View, nối bằng một mũi tên có nhãn "quy tắc"; token có mũi tên đậm "tự động".
---

### PROCESS · Build order
- Kicker: Quy trình
- Title: Rules, shell, flow, build, review
- On-slide:
  - Rules: viết hoặc nhận rules file trước
  - Shell: dựng màn hình số 0, khung trống
  - Flow: đưa flow từ tuần 4 vào, không để AI tự nghĩ
  - Build: AI dựng journey trong shell
  - Review: bạn mở file và mở trang ra dùng
- Ví dụ: có (delivery app: rules, header và menu, flow đặt đồ ăn năm màn, dựng, review)
- Câu hỏi hay gặp:
  - Dựng cả journey một lượt hay từng màn? Chương trình dạy dựng cả journey sau khi có rules và shell; các gate của skill dùng để kiểm.
  - Vì sao không để AI nghĩ flow? Flow là quyết định thiết kế đã có từ tuần 4.
- Speaker notes:

  > Với delivery app: mình viết rules, dựng khung header và menu trống, đưa vào flow đặt đồ ăn năm màn đã có, để AI dựng, rồi mở từng file để review.

  - Thứ tự là phương pháp của chương trình: rules trước, rồi shell, rồi flow, rồi dựng, rồi review
  - Màn hình số 0 là shell trống; kiểm ở độ rộng điện thoại và máy tính trước khi dựng tiếp
  - Flow đến từ tuần 4, không phải AI nghĩ ra
  - Chưa có nghiên cứu đo hiệu quả của thứ tự này
  - Skill prototype của toolkit có các gate kiểm; bạn dùng nó ở Practice 5

  > **Review là bước dài nhất, vì một lượt dựng cả journey cho ra nhiều chỗ cần sửa.**

  > Trong năm bước, bước nào bạn thường bỏ khi làm vội?
- 🎨 Visual hint: SCHEMATIC. Process năm bước; bước Review tô active.
---

### DIAGRAM · Right layer
- Kicker: Cách làm
- Title: Fix at the right layer
- On-slide:
  - Hỏi: lỗi này có sai ở nhiều hơn một màn không?
  - Sửa ở layer rộng nhất mà lỗi còn đúng
  - Token, component, shell, template, màn hình
  - Fix too low: lỗi quay lại ở từng màn
  - Push too high: hệ thống mang thứ một màn cần
- Ví dụ: có (nút màu cam ở cả năm màn của delivery app: sửa ở token và rules file, không sửa năm màn)
- Câu hỏi hay gặp:
  - Vì sao shell nằm trong ladder? Ladder gốc ở lesson Scaling the Prototype có bốn bậc; shell được xếp thêm theo phần shared layout của cùng lesson `[to confirm]`.
  - Lỗi ở một màn thì sao? Sửa ngay ở màn đó, đừng đẩy lên hệ thống.
- Speaker notes:

  > Nút màu cam xuất hiện ở cả năm màn của delivery app. Nếu sửa từng màn, màn sau sẽ lại cam. Câu hỏi để bạn tự dùng khi không có mình: lỗi này có sai ở nhiều hơn một màn không?

  - Ladder từ rộng đến hẹp: token (mọi màn), component (mọi chỗ dùng), shell (mọi loại màn), template (mọi màn cùng loại), màn hình (chỉ màn đó)
  - Quy tắc: sửa ở layer rộng nhất mà lỗi còn đúng, không phải layer rộng nhất có thể
  - Fix too low là cách sai quen thuộc: thực chất vẫn là dựng từng màn một
  - Push too high ít ai cảnh báo: hệ thống chứa đầy những thứ chỉ một màn cần
  - Một màn không dẫn đi đâu thì sửa ở flow, không sửa ở layer nào của ladder
  - Đây là layer ladder của lesson Scaling the Prototype; việc xếp shell vào ladder là điều chỉnh của mình

  > **Sửa ở layer rộng nhất mà lỗi còn đúng. Không phải layer rộng nhất có thể.**

  > Lỗi nào bạn từng sửa đi sửa lại ở nhiều màn?
- 🎨 Visual hint: SCHEMATIC. Ladder năm bậc xếp dọc (token, component, shell, template, màn hình), mỗi bậc kèm phạm vi ảnh hưởng; hai mũi tên ghi "fix too low" và "push too high".
---

### DIAGRAM · Link
- Kicker: Cách kiểm
- Title: Requirement gắn vào element
- On-slide:
  - Mỗi requirement có một ID: R1, R2, R3
  - Mỗi element mang ID của requirement nó thể hiện
  - Requirement chưa có element nào là chỗ hở
  - Người duyệt quyết định: bổ sung hay bỏ requirement
- Ví dụ: có (delivery app, màn thanh toán: R1 mã giảm giá và R2 thanh toán một chạm đã có element; R3 hiển thị phí vận chuyển chưa có element nào)
- Câu hỏi hay gặp:
  - Requirement lấy từ đâu? Dòng ngắn rút từ problem brief và hướng đã chọn `[to confirm]`.
  - Cách này là chuẩn ngành? Không; đây là một cách một số designer dùng, chưa có nguồn công khai `[to confirm]`.
- Speaker notes:

  > Màn thanh toán của delivery app có ba requirement. AI dựng xong, màn hình trông đủ: có ô mã giảm giá, có nút Thanh toán. Phí vận chuyển ở đâu?

  - Một số designer gắn ID requirement vào từng element của prototype
  - Ô nhập mã mang R1, nút Thanh toán mang R2
  - R3, phí vận chuyển, không element nào mang: đó là chỗ hở
  - Màn hình trông đủ vẫn có thể thiếu một thứ nó phải có
  - Ngược lại, element không mang ID nào thì hỏi: nó thể hiện requirement nào?
  - AI gắn ID và liệt kê chỗ hở; người duyệt quyết định bổ sung hay bỏ requirement đó
  - Đây là cách một số designer đang làm, chưa phải chuẩn ngành

  > **Requirement chưa có element nào gắn là chỗ hở, và chỗ hở đó do bạn quyết, không phải AI.**

  > Trong flow của bạn, bạn có thể liệt kê ba requirement nào cho màn quan trọng nhất? Gõ vào chat một requirement.
- 🎨 Visual hint: DIAGRAM. Dùng `assets/ai-pattern-link.html`: prototype bên trái, requirement bên phải, nối bằng ID; R3 màu coral là chỗ hở.
---

### COMPARE · Prototype is
- Kicker: Giới hạn
- Title: Prototype là gì, không là gì
- On-slide:
  - Là: bản tham chiếu cho developer, thứ để test với người dùng
  - Không là: code production, bằng chứng rằng thiết kế đúng
  - Chạy được: ý tưởng có thể hoạt động, chưa phải đã hoạt động
  - Đi cùng prototype: link chạy được, rules file, điều chưa làm
- Ví dụ: có (delivery app: prototype chạy được cho thấy flow đặt đồ ăn có thể hoạt động, chưa cho biết người dùng có chọn đúng thời gian giao hay không)
- Câu hỏi hay gặp:
  - Prototype có thể là final design không? Plan ghi "có thể là final design"; mức hoàn thiện cần chốt cho Practice 5 `[to confirm]`.
- Speaker notes:

  > Prototype của delivery app chạy được: bạn bấm qua năm màn, đặt được một đơn giả. Điều đó chưa nói người dùng có hiểu màn chọn thời gian giao hay không.

  - Prototype là bản tham chiếu cho developer và thứ để test
  - Không phải code production
  - Chạy được chỉ cho thấy ý tưởng có thể hoạt động
  - Buổi test ở tuần 6 mới cho thấy nó có hoạt động
  - Mức hoàn thiện cần có để đem đi test sẽ chốt ở Practice 5
  - Khi chuyển cho người khác, ba thứ đi cùng: link chạy được, rules file và danh sách điều chưa làm
  - Lesson handoff đã bỏ khỏi chương trình; hôm nay chỉ nêu ba thứ này ở mức khái niệm

  > **Một prototype chạy được là một thứ để test, không phải một kết quả.**

  > Câu hỏi 30 giây: nút màu cam xuất hiện ở cả bốn màn. Sửa ở đâu trước? A, từng màn. B, ở layer rộng nhất mà lỗi còn đúng, ví dụ token. Gõ A hoặc B vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Compare hai cột "Là" và "Không là", dòng cuối nổi bật.
---

### NUMBERED · Gate, Rules, Skill
- Kicker: Kiểm soát
- Title: Gate, Rules, Skill
- On-slide:
  - Gate: điểm dừng kiểm tra giữa các bước
  - Rules: quy tắc AI đọc trước mỗi lần dựng
  - Skill: step card mà AI tool làm theo
- Ví dụ: có (Atlassian cài skill vào repo kèm chỉ dẫn trong AGENTS.md [3]; Uber dùng một skill cho mỗi mục spec [9])
- Câu hỏi hay gặp:
  - Skill khác rules file thế nào? Rules là quy tắc cố định; skill là các bước và prompt của một quy trình.
  - Gate có phải review không? Gate là điểm dừng; review là việc bạn làm ở một gate.
- Speaker notes:

  > Atlassian cài bộ skill vào repo và thêm một chỉ dẫn ngắn trong AGENTS.md để mọi agent dùng chung. Uber dùng một skill riêng cho mỗi mục của spec.

  - Gate là điểm dừng kiểm tra giữa các bước; skill prototype có nhiều gate, mỗi gate kiểm xong mới đi tiếp
  - Rules là rules file; AI đọc nó trước mỗi lần dựng
  - Skill là step card: các bước và prompt mà AI tool làm theo, để quy trình lặp lại được
  - Cả ba cùng một mục đích: quy trình không nằm trong trí nhớ của một người
  - Ba lớp này chạy xuyên cả One View và The Second View, và được đặt trước khi dựng

  > **Quy tắc và gate được đặt trước khi dựng, không thêm vào sau.**

  > Quy trình nào của bạn đang nằm trong đầu bạn mà chưa viết ra?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered lưới ba cột, ba ô: Gate, Rules, Skill; mỗi ô một dòng mô tả.
---

### NUMBERED · System rules
- Kicker: Rules file
- Title: System rules
- On-slide:
  - 1. Chỉ dùng component trong inventory; thiếu thì thêm trước
  - 2. Không dùng giá trị thô: chỉ dùng token, báo cái chưa có
  - 3. Màn hình kế thừa template, nằm trong shell
  - 4. Mỗi lần dựng mang theo flow context
  - 5. Nội dung thật, đúng content voice, không lorem ipsum
- Ví dụ: có (delivery app: công tắc chưa có trong inventory, nên quy tắc 1 bắt AI dừng và yêu cầu thêm công tắc vào inventory trước)
- Câu hỏi hay gặp:
  - Vì sao quy tắc 2 có vế "báo cái chưa có"? Để một token còn thiếu không biến thành một mã màu tự bịa mà trông vẫn ổn.
  - Quy tắc nào quan trọng nhất? Quy tắc 1 đến 3; quy tắc 1 và 2 cùng trả lời câu "đừng dùng gì ngoài design system".
- Speaker notes:

  > Một rules file cho delivery app có quy tắc 1: thiếu component trong inventory thì yêu cầu thêm trước, rồi mới dựng. AI đọc quy tắc đó trước mỗi lần dựng.

  - Mười quy tắc chia hai nhóm: năm quy tắc hệ thống ở slide này, năm quy tắc làm việc ở slide kế
  - Không đọc hết năm quy tắc; nhấn ba quy tắc đầu
  - Quy tắc 1 và 2 cùng trả lời câu "đừng dùng gì ngoài design system"
  - Vế sau của quy tắc 2 ngăn một token còn thiếu biến thành một mã màu tự bịa mà trông vẫn ổn
  - Quy tắc 3 giúp cập nhật thay đổi xuống các màn hình về sau; mình thêm "nằm trong shell" vào quy tắc gốc
  - Quy tắc 5 có thêm "đúng content voice đã chốt", theo content voice ở slide One View

  > **Quy tắc 1 và 2 là toàn bộ câu trả lời cho: đừng dùng gì ngoài design system.**

  > Trong năm quy tắc này, quy tắc nào bạn chưa từng viết cho AI?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered lưới năm ô, mỗi ô một quy tắc; ba quy tắc đầu tô nổi.
---

### NUMBERED · Working rules
- Kicker: Rules file
- Title: Working rules
- On-slide:
  - 6. Mỗi lần sửa một layer, nêu tên layer
  - 7. Chỉ đính kèm file mà bước đó cần
  - 8. Báo, không bịa: kết thúc bằng điều chưa làm được
  - 9. Lưu trước khi sửa cấu trúc
  - 10. WCAG 2.1 AA mọi màn: tương phản, focus, vùng chạm
- Ví dụ: có (delivery app: sửa màn danh sách thì chỉ đính kèm shell và template danh sách, không đính kèm cả folder)
- Câu hỏi hay gặp:
  - Vì sao đính kèm ít file hơn? Thêm file không giúp hơn; nó chỉ mở rộng phạm vi tool có thể sửa.
  - WCAG ở đây có phải là một buổi audit không? Không; đây là quy tắc áp lúc dựng. Áp lúc dựng không tốn gì, kiểm tra sau thì tốn cả một buổi.
- Speaker notes:

  > Bạn đính kèm cả folder để AI hiểu rõ hơn. Kết quả thường ngược lại: AI có thêm nhiều file để sửa nhầm.

  - Năm quy tắc làm việc nói về cách học viên và tool cư xử, khác năm quy tắc hệ thống ở slide trước
  - Nhấn quy tắc 7 và quy tắc 10, để slide tự nói phần còn lại
  - Quy tắc 7 ngược trực giác: thêm context không giúp, nó chỉ mở rộng phạm vi tool có thể sửa
  - Quy tắc 10: màn do AI dựng thường có focus không nhìn thấy và độ tương phản sát ngưỡng
  - Quy tắc 9: "lưu" là lưu một checkpoint; skill prototype dùng lệnh "Lưu lại"
  - Quy tắc 8: mỗi lần dựng kết thúc bằng những gì AI chưa làm được, để bạn không phải đoán

  > **Áp quy tắc lúc dựng không tốn gì. Kiểm tra sau thì tốn cả một buổi.**

  > Quy tắc nào trong năm quy tắc này bạn sẽ khó giữ nhất?
- 🎨 Visual hint: TYPOGRAPHIC. Numbered lưới năm ô, mỗi ô một quy tắc; quy tắc 7 và 10 tô nổi.
---

### STATEMENT · Rules you rewrite
- Kicker: Nguyên tắc
- Title: Rules you\n*rewrite* are yours
- On-slide: Quy tắc nhận từ người khác chưa thuộc về bạn
- Ví dụ: có (một quy tắc mẫu "dùng màu chính cho nút chính" bị AI phá vì không nói rõ "mọi nút chính", nên học viên viết lại)
- Câu hỏi hay gặp:
  - Rules file có lệch khi đổi design system không? Có; khi thêm component hoặc đổi token, cập nhật design-system notes và rules file trong cùng lượt.
- Speaker notes:

  > Bạn nhận bộ mười quy tắc từ mình. Sau lần dựng đầu, bạn sẽ thấy dòng nào AI vẫn vi phạm, dòng nào thiếu. Dòng bạn viết lại bằng lời của mình mới là dòng của bạn.

  - Bộ quy tắc mẫu đến từ kinh nghiệm của người khác
  - Quy tắc chỉ thuộc về bạn sau khi bạn dựng một lần và thấy quy tắc nào thiếu
  - Rules file và design system có thể lệch nhau khi một bên đổi mà bên kia không đổi
  - Một nguồn agency báo rủi ro này; đó là kinh nghiệm của một agency, chưa phải kết quả đo
  - Quy tắc của chương trình: thêm component hoặc đổi token thì cập nhật cả hai trong cùng lượt
  - Quy tắc không bắt được gì chưa chắc là sai: đánh dấu, đừng xoá, xem lại sau journey thứ hai
  - Quy tắc nào chưa có thì viết thêm bằng lời của bạn, đặt ở đầu danh sách

  > **Quy tắc bạn viết lại bằng lời của mình mới là quy tắc của bạn.**

  > Câu hỏi 30 giây: khi thiếu component, rules file nên nói gì? A, tạo cái gần giống nhất. B, dừng và hỏi. Gõ A hoặc B vào chat.
- 🎨 Visual hint: TYPOGRAPHIC. Statement layout; một dòng, accent ở "rewrite".
---

### MILESTONE · Break and check
- Num: 4
- Kicker: Bridge
- Title: Break,\n*then check*
- Sub: Nghỉ ngắn, hai câu kiểm tra, cheat sheet
- Speaker notes:

  > Nghỉ hai phút. Quay lại, mình hỏi hai câu nhanh, rồi cheat sheet ở lại trên màn hình đến hết buổi.

  - Hai phút nghỉ, rồi hai câu kiểm tra nhanh hỏi miệng
  - Câu một: bốn layer của Design Pattern là gì và layer nào là của product
  - Câu hai: vì sao báo cáo của AI rằng một màn hình đã xong không đủ
  - Cheat sheet một màn hình ở slide kế

  > **Câu nào bạn chưa chắc, ghi vào chat để mình quay lại ở phần hỏi đáp.**

  > Mình mở cheat sheet.
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số 4 lớn.
---

### DIAGRAM · Cheat sheet
- Kicker: Tham khảo
- Title: Cheat sheet
- On-slide:
  - Bốn layer: token, component, shell, template; cả bộ là Design Pattern
  - Mười quy tắc: năm cho hệ thống, năm cho cách làm việc
  - Sau khi dựng: mở file, mở trang, đối chiếu quy tắc, kiểm hai độ rộng
- Ví dụ: Không cần. Slide tham khảo, nhắc lại nội dung đã có.
- Câu hỏi hay gặp:
  - Tài liệu này gửi sau buổi không? Có.
- Speaker notes:

  > Một màn hình để bạn quay lại khi làm ở buổi practice.

  - Bốn layer ở trên cùng
  - Mười quy tắc rules file ở giữa
  - Các bước kiểm sau khi dựng ở dưới cùng
  - Slide này ở lại trên màn hình trong activity và hỏi đáp
  - Mình gửi bản này sau buổi học

  > **Mọi thứ trên slide này đã nói trong buổi; không có nội dung mới.**

  > Có dòng nào trên đây bạn chưa hiểu?
- 🎨 Visual hint: SCHEMATIC. Một màn hình, ba khối: bốn layer, mười quy tắc, các bước kiểm; chữ nhỏ đọc được trong một cái nhìn.
---

### MILESTONE · Rule-break hunt
- Num: 5
- Kicker: Activity
- Title: Find the\n*three breaks*
- Sub: Ba quy tắc hệ thống, một màn hình, ba lỗi
- Speaker notes:

  > Đây là màn hình AI vừa dựng cho một delivery app. Nhìn thoáng thì ổn. Mình dán ba quy tắc hệ thống bên cạnh. Trong hai phút, bạn tìm giúp mình ba chỗ vi phạm quy tắc. Chưa nói to, ghi ra trước.

  - Năm phút: 30 giây giới thiệu, 2 phút tự tìm, 1,5 phút lộ đáp án, 1 phút nối sang dự án của bạn
  - Nói rõ có đúng ba lỗi, và có vài chỗ trông lạ nhưng đúng quy tắc
  - Không gợi ý khi học viên tìm; mục đích là tự thấy việc đối chiếu cần quy tắc viết sẵn
  - Quy tắc cắt: nếu trễ thì bỏ phần tự tìm, chiếu đáp án luôn

  > **Đối chiếu với quy tắc, không đoán theo cảm giác.**

  > Mình chiếu màn hình.
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số 5 lớn.
---

### IMAGE · The screen
- Kicker: Màn hình
- Title: Chọn thời gian giao
- On-slide: Màn hình mẫu ở độ rộng điện thoại, cạnh ba quy tắc hệ thống
- Ví dụ: bản nháp (màn hình `screen.html` của delivery app, hư cấu, ba lỗi cài sẵn; đáp án giảng viên ở `_instructor-only-error-key.md`)
- Câu hỏi hay gặp:
  - Có đúng ba lỗi không? Có; ngoài ra có vài chỗ trông lạ nhưng đúng quy tắc (thẻ Phổ biến, khối thông báo, chỉ báo bước).
- Speaker notes:

  > Hai phút. Ghi ba chỗ vi phạm quy tắc ra giấy hoặc chat. Chưa nói.

  - Chiếu màn hình ở độ rộng điện thoại, cùng ba quy tắc hệ thống (quy tắc 1 đến 3)
  - Học viên tự tìm trong hai phút
  - Không nói đáp án và không gợi ý trong lúc này
  - Mở sẵn `components.html` để đối chiếu khi lộ đáp án

  > **Có đúng ba lỗi. Có vài chỗ trông lạ nhưng đúng quy tắc.**

  > Mình mở đáp án.
- 🎨 Visual hint: REAL. Ảnh chụp `assets/templates/rule-break-hunt/screen.html` ở độ rộng điện thoại `[to confirm]`: cần mở file và chụp trước buổi dạy.
---

### DIAGRAM · Three breaks
- Kicker: Đáp án
- Title: Ba lỗi, ba quy tắc
- On-slide:
  - Thanh điều hướng thứ hai ở đáy: quy tắc 3, mọi màn nằm trong shell
  - Nút màu cam: quy tắc 2, chỉ dùng token
  - Công tắc ngoài hệ thống: quy tắc 1, thiếu thì thêm trước
  - Trông lạ nhưng đúng: thẻ Phổ biến, khối thông báo, chỉ báo bước
- Ví dụ: có (màn hình `screen.html` của delivery app)
- Câu hỏi hay gặp:
  - Thẻ Phổ biến có phải lỗi không? Không; nó là component có sẵn. Đối chiếu với `components.html`.
- Speaker notes:

  > Lỗi một: thanh điều hướng tối ở đáy, trong khi header đã có điều hướng. Lỗi hai: nút "Tiếp tục" màu cam, trong khi màu chính là xanh lá. Lỗi ba: công tắc "Giao không tiếp xúc", không có trong danh sách component.

  - Mỗi lỗi lộ xong, hỏi "quy tắc nào bị phá" và "tìm nó trong file bằng cách nào"
  - Cách tìm: tìm `nav` và `tabbar`; tìm `#` trong thuộc tính style; đối chiếu `components.html`
  - Lỗi một và ba còn kéo theo màu thô: một thứ AI tự bịa thường kéo theo thứ khác
  - Thẻ Phổ biến, khối thông báo và chỉ báo bước đúng quy tắc; hỏi "chỗ này có trong components.html không?"
  - Nối lại bảng lỗi ở ice breaker: kiểu lỗi nào hôm nay gặp lại

  > **Báo cáo của AI chỉ là bản tóm tắt. Bằng chứng là trang bạn mở ra và so với quy tắc.**

  > Trong prototype của bạn, chỗ nào AI có thể âm thầm làm đúng như vậy mà bạn chưa kiểm?
- 🎨 Visual hint: SCHEMATIC. Bảng ba hàng (lỗi, quy tắc bị vi phạm, cách tìm) và một hàng riêng "Trông lạ nhưng đúng".
---

### MILESTONE · Q&A
- Num: 10
- Kicker: Hỏi đáp
- Title: Questions\n*in the chat*
- Sub: Cheat sheet ở lại trên màn hình
- Speaker notes:

  > Mười phút cho câu hỏi. Mình đọc từ chat, bắt đầu với những câu bạn ghi lúc nghỉ.

  - Câu hỏi học viên ghi trong chat suốt buổi
  - Ưu tiên câu liên quan đến design system và dữ liệu của công ty
  - Nếu hỏi về tinh chỉnh state, accessibility, principle audit: nói đây là việc ở Practice 5
  - Nếu hỏi về số liệu hiệu quả: nói thẳng là chưa có số đo độc lập

  > **Câu nào chưa có số đo, mình nói thẳng là chưa có.**

  > Câu hỏi đầu tiên là gì?
- 🎨 Visual hint: TYPOGRAPHIC. Milestone layout nền purple, số 10 lớn; cheat sheet thu nhỏ ở góc.
---

### PRACTICE · Practice
- Kicker: Việc tiếp theo
- Title: Practice 5
- On-slide:
  - Bạn áp dụng bốn layer và mười quy tắc lên flow của chính bạn
  - Việc chuẩn bị và các bước nằm trong practice sheet
  - Mang hướng đã chọn, flow và nội dung thật
  - Cuối bài, ghi ba dòng vào learning log
- Ví dụ: Không cần. Slide giao việc.
- Speaker notes:

  > Hôm nay bạn đã có bốn layer và mười quy tắc của rules file. Ở Practice 5, bạn dùng đúng chúng trên flow của chính bạn.

  - Việc chuẩn bị và các bước cụ thể nằm trong practice sheet, mình gửi riêng
  - Hướng đã chọn và flow là đầu ra của tuần 4
  - Design system của công ty có thể là tài liệu mật; không chắc thì dùng bản của mình
  - Cuối bài, bạn ghi learning log ba dòng và trả lời một câu reflection

  > **Shell và template của product là phần bạn tự định nghĩa; AI không làm thay.**
- 🎨 Visual hint: TYPOGRAPHIC. Một card "Practice 5" với ba dòng: áp dụng, practice sheet, learning log.
---

### END
- Kicker: End
- Title: Thank *you*
- Sign: Winnie Nguyen
- Contact: Buổi tiếp theo, Practice 5
- Speaker notes:
  - Cảm ơn cả lớp
  - Nhắc lại: Practice 5 dùng bốn layer và mười quy tắc của hôm nay
  - Gửi cheat sheet sau buổi học
- 🎨 Visual hint: End layout, nền paper-deeper; title lớn nghiêng, tên bên dưới.
