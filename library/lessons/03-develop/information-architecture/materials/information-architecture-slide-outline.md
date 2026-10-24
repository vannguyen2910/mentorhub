---
title: "Information Architecture"
lesson_file: "information-architecture-lesson.md"
level: ""
slide_count: 47
duration: "120–135 min"      # [to confirm] khớp với lesson cũ; deck không ghi tổng giờ
status: matches-built-deck
built_deck: "Information Architecture (VIE).dc.html (Claude Design; chưa nằm trong repo)"
last_synced: 2026-10-23
---

> **Source of truth:** `information-architecture-lesson.md`
> Outline này được reverse-sync từ deck 47 slide (deck wins, theo Deck edit rule trong `CLAUDE.md`). Bản cũ nằm ở `_archive/information-architecture-slide-outline-pre-deck-sync-2026-10-23.md`.
> Phần 1 (slide 5 đến 10) đã được viết lại theo format speaker notes mới. Slide còn lại mang nguyên notes từ deck và chưa chuyển sang dòng nguyên văn.

---

## Session metadata

| Field | Value |
|---|---|
| Program | private-training / ux-class `[to confirm]` |
| Track / session | Deck ghi "Buổi 5"; lesson cũ ghi session 04 (ui-ux-fundamentals) và 05 (junior-to-mid-level) `[to confirm]` |
| Stage | Develop |
| Prior session | Synthesis & Problem Definition |
| Next session | Design |
| Running example | Food delivery (sitemap, card sort, tree test, user flow, process map) |

---

## Slide structure — 47 slides

- Arc: **Open** (slide 1 đến 4) → **Phần 1** Inherited vs Evidence-Based (5 đến 10) → **Phần 2** Card Sorting (11 đến 16) → **Phần 3** Tree Testing (17 đến 22) → **Phần 4** User Flows (23 đến 31) → **Phần 5** Process Map (32 đến 40) → **Phần 6** Defend Your IA (41 đến 44) → **AI trong thực tế** (45) → **Close** (46, 47).
- Thời lượng theo deck: Phần 1 đến 3 mỗi phần 7 phút; Phần 4 = 8 phút (nâng từ 6 phút của deck, 2026-10-23); Phần 5 = 9 phút (nâng từ 6 phút của deck, 2026-10-23); Phần 6 = 6 phút (tổng 44 phút nội dung). Activity: Build 1 = 10, Build 2 = 9, Build 3 = 8, Hoạt động 1 = 20, Hoạt động 2 = 15, Bảo vệ = 10 (tổng 72 phút). Mở bài khoảng 4 đến 5 phút. `[to confirm]` giả định phút của các Phần không gồm activity; tổng cộng khoảng 121 đến 126 phút, so với khung 120 đến 135 phút của lesson cũ.
- Deck gộp MILESTONE và task card vào một slide `PRACTICE` (số phút nằm trên chính slide). Template mặc định tách hai slide; giữ theo deck.
- Kicker và Title đã rà theo quy tắc mới (2026-10-23): Title là nhãn chủ đề tối đa 6 từ, Kicker nêu vai trò slide và không mang số Phần hay Buổi. Đã sửa 31 slide trong cả deck và outline. Câu nhận định cũ (ví dụ "Nhiều actor, một kết quả") nằm trong On-slide hoặc speaker notes nếu đã có ở đó; chưa chuyển thêm.
- Phần 4 đã nâng lên 8 phút cho 8 slide (23 đến 30), mỗi slide 1 phút. Deck vẫn ghi 6 phút ở slide 4 và 23, cần sửa deck.
- Phần 5 đã nâng lên 9 phút cho 8 slide (32 đến 39): bảy slide mỗi slide 1 phút, slide 39 là 2 phút. Deck vẫn ghi 6 phút (slide 4, 23 và 32), cần sửa deck. Slide 39 trong deck có khoảng 25 bullet; outline đã gom còn 8, nên vẫn nên tách thành hai slide.
- Slide 3 và 39 nêu tên app thật (Grab, ShopeeFood, Be); quy tắc ví dụ generic cần xem lại `[to confirm]`.

---

## Slides

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Develop
- Title: Information\n*Architecture*
- Subtitle: Cấu trúc từ bằng chứng, và cách thuyết phục người khác thay đổi nó.
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer at NAB
  - Master of UX & Service Design
  - Giảng viên Product Design
- Right panel photo: theo deck (slide 01)
- Speaker notes:

  > Buổi trước mình chốt xong vấn đề. Hôm nay mình mở phần giải pháp, ở cấp độ cấu trúc.

  - Mở bài dài một phút
  - Nhắc lại một câu chẩn đoán của buổi trước để mentee định vị
  - Không vẽ màn hình; mọi thứ hôm nay là cây, bộ thẻ, luồng hoặc hồ sơ quyết định
  - Đầu ra duy nhất là ia-decision-record.md, kèm một lần pitch cho chủ sở hữu mục bạn muốn dời

  > **Cuối buổi, bạn bảo vệ phương án trước người sở hữu mục bạn muốn dời.**

  > Ai đã thử vẽ lại menu của sản phẩm mình đang làm?

- 🎨 Visual hint: theo deck (slide 01).

---

### STATEMENT · Buổi trước mình dừng ở đâu
- Kicker: Buổi trước mình dừng ở đâu
- Title: Brief của bạn đã nói vấn đề là gì.
- On-slide: Nhưng chưa nói mọi thứ đang nằm ở đâu. | Kết luận chẩn đoán, giờ đặt lại thành một câu hỏi về cấu trúc.
- Giờ: 1 phút (theo deck: dưới 1 phút)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Mình mời bạn đọc to bản chẩn đoán của buổi trước, giữ nguyên chữ.

  - Nếu mentee chưa nhớ câu chẩn đoán, mở lại brief ở màn hình khác, không đọc thay họ
  - Mục đích slide là chuyển từ "vấn đề là gì" sang "vấn đề nằm ở đâu trong cấu trúc"
  - Câu trả lời thường gặp: ở ba nơi, của ba team; đó là chất liệu của hôm nay

  > **Vấn đề này đang nằm ở đâu trong sản phẩm?**

  - Dừng năm giây im lặng sau câu hỏi

- 🎨 Visual hint: theo deck (slide 02).

---

### NUMBERED · Câu hỏi năm cách
- Kicker: Câu hỏi năm cách
- Title: Đơn còn đang tới không?
- On-slide: Khi đơn đang trên đường giao… | 01 | Một trang trạng thái, vào từ mục Orders | 02 | Màn hình Home trở thành đơn đang giao | 03 | Không có trang riêng, notification báo thay | 04 | Nằm trong Help, dưới tên "đơn của tôi đâu" | 05 | Một status bar hiện trên mọi màn hình cho tới khi đơn tới | Chat với tài xế không phải đáp án thứ sáu, vì nó nằm ngoài phạm vi (non-goal).
- Giờ: 2 phút (theo deck, nói miệng, không viết)
- Ví dụ: bản nháp (khách đặt pizza lúc 19:00, đến 19:35 vẫn chưa thấy). Cần ví dụ thật: mở hai app giao đồ ăn thật trên điện thoại, cho thấy mỗi app đặt "đơn đang giao" ở một chỗ khác nhau; chụp trước hai ảnh màn hình để so sánh
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Khách đặt pizza lúc 19:00, đến 19:35 vẫn chưa thấy. Lúc này bạn mở app và bấm vào đâu?

  - Có người sẽ bấm Home, có người bấm Orders, có người bấm Help; chính sự chia phe này là lý do có năm cấu trúc
  - Một chẩn đoán, năm cấu trúc khác nhau; mỗi cái có sitemap, nhãn và chủ sở hữu riêng
  - Đọc lần lượt năm cách, mỗi cách khoảng 15 giây
  - Chat với tài xế không phải đáp án thứ sáu, vì nó thuộc một câu hỏi khác (giao tiếp), không phải câu hỏi cấu trúc: đây là non-goal trong brief

  > **Chưa ai được chọn. Cả buổi là cách chọn bằng bằng chứng.**

  > Theo trực giác, bạn chọn cách nào? Mình ghi lại để so với kết quả cuối buổi.

  > Hãy nêu năm cách của riêng bạn, từ brief của bạn.

- 🎨 Visual hint: theo deck (slide 03).

---

### NUMBERED · Buổi 5 · System Architecture & IA
- Kicker: Tổng quan buổi
- Title: Mục tiêu buổi học
- On-slide: 01 | Inherited vs evidence-based: vẽ lại những gì đang có | 02 | Card sorting: xem khách hàng tự nhóm thế nào | 03 | Tree testing: kiểm tra xem cấu trúc có dùng được không | 04 | User flow: xem cấu trúc này bắt user trả giá những gì | 05 | Process map: xem ai làm gì phía sau màn hình | 06 | Bảo vệ IA: thuyết phục chính người đang sở hữu nó
- Giờ: 1 phút (đề xuất)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Hôm nay có sáu phần, đi theo thứ tự từ 01 đến 06. Mình nói thời lượng từng phần để bạn tự canh.

  - Phần 1 là 7 phút, Phần 2 là 7 phút, Phần 3 là 7 phút, Phần 4 là 8 phút, Phần 5 là 9 phút, Phần 6 là 6 phút (đã cập nhật so với deck)
  - Thứ tự có lý do: vẽ cây hiện tại trước khi sort, vì thẻ card sort lấy từ sitemap
  - Bốn phần build, một phần bảo vệ ở cuối

  > **Bạn đi từ một câu hỏi đến một quyết định bạn bảo vệ được.**

- 🎨 Visual hint: theo deck (slide 04).

---

### SECTION DIVIDER · Inherited vs Evidence-Based
- Num: 01
- Kicker: Inherited vs Evidence-Based
- Title: Inherited vs Evidence-Based
- Sub: Hầu hết designer nhận IA có sẵn rồi dùng luôn, không hỏi lại.
- Giờ: 1 phút (đề xuất; cả Phần 1 là 7 phút theo deck)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Phần đầu chỉ có một mục tiêu: bạn tự nhận ra dấu hiệu sơ đồ tổ chức trong chính sản phẩm của mình.
  - Đây là phần ngắn nhất; không sa vào định nghĩa

  > **Hầu hết designer thừa hưởng IA và không bao giờ đặt câu hỏi.**
  - Chuẩn bị sẵn một câu hỏi dẫn để mentee tự trả lời ở slide kế tiếp

  > Mục nào trong menu của bạn chỉ giải thích được bằng tên team?

- 🎨 Visual hint: theo deck (slide 05).

---

### STATEMENT · Định nghĩa
- Kicker: Định nghĩa
- Title: IA quyết định\n*cái gì nằm ở đâu*
- On-slide: Tên gọi là gì, và đi tới đó bằng cách nào.
- Giờ: 1 phút (đề xuất)
- Ví dụ: bản nháp (menu ngân hàng xếp theo dòng sản phẩm: Cards, Loans, Savings). Cần ví dụ thật: một case IA thừa hưởng từ dự án của Winnie, đã ẩn thông tin nhạy cảm
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Một app ngân hàng có mục Cards, Loans, Savings, vì mỗi mục do một team sản phẩm giữ. Khách chỉ hỏi: tiền của tôi đang ở đâu?
  - Không định nghĩa IA dài dòng với người đã senior
  - IA quyết định ba thứ: cái gì nằm ở đâu, tên gọi là gì, và đi tới đó bằng cách nào

  > **Câu hỏi quan trọng là: ai quyết định?**
  - Dừng sau câu hỏi này và để mentee trả lời; họ thường nói "PO" hoặc "không biết", cả hai đều đưa được vào slide sau

  > Sản phẩm của bạn có mục nào đặt tên theo team không?

  > Làm sao phân biệt cấu trúc thừa hưởng với cấu trúc có bằng chứng? Slide sau trả lời.

- 🎨 Visual hint: theo deck (slide 06).

---

### COMPARE · Điểm khác biệt cốt lõi
- Kicker: So sánh
- Title: Hai cách làm IA
- On-slide: Inherited IA | Nguồn: | PO, stakeholder, hệ thống cũ | Logic: | theo team, theo quyền sở hữu tính năng, theo hệ thống | Rủi ro: | "nghe hợp lý với bên mình" | Evidence-Based IA | Nguồn: | card sort, tree test, dữ liệu search và support | Logic: | theo mental model và task của user | Rủi ro: | cần thời gian và kỷ luật phương pháp | Cách nhận ra: nếu một mục chỉ có lý khi bạn nói ra ai sở hữu nó, thì đó là cấu trúc inherited.
- Giờ: 2 phút (đề xuất)
- Ví dụ: bản nháp (Support, Orders, Account so với Đơn của tôi, Sự cố với đơn, Thanh toán). Cần ví dụ thật: cặp ảnh một menu inherited và một menu sau khi test; ReferPlus ở slide 15 và 21 có thể dùng làm cặp này
- Câu hỏi hay gặp:
  - Inherited có phải luôn sai không? Không; chỉ là chưa được kiểm chứng.
  - Có phải lúc nào cũng làm evidence-based đủ bộ không? Không; nó tốn thời gian nên không phải lúc nào cũng làm đủ.
- Speaker notes:

  > Inherited: Support, Orders, Account, ba team. Evidence-based: Đơn của tôi, Sự cố với đơn, Thanh toán, ba việc khách muốn làm. Cùng nội dung, khác cách chia.
  - Inherited: nguồn là PO, stakeholder, hệ thống cũ; logic theo team; rủi ro là "nghe hợp lý với bên mình"
  - Evidence-based: nguồn là card sort, tree test, dữ liệu search và support; logic theo mental model; rủi ro là cần thời gian và kỷ luật phương pháp
  - Evidence-based không phải ý kiến của designer, nên mới có cột nguồn

  > **Nếu một mục chỉ có lý khi bạn nói ra ai sở hữu nó, thì đó là cấu trúc inherited.**
  - Đọc câu in đậm hai lần; đây là điều mang về từ Phần 1

  > Sản phẩm của bạn đang ở cột nào? Mục cấp 1 nào qua được bài kiểm tra này?

- 🎨 Visual hint: theo deck (slide 07).

---

### NUMBERED · Phương pháp · Sitemap
- Kicker: Định nghĩa
- Title: Sitemap là gì?
- On-slide: Là gì | Mọi màn hình và mục user đang chạm vào hôm nay, xếp lồng nhau từ cha đến con, đúng như sản phẩm thật. | Để làm gì | Chưa kiểm kê nội dung thì không viết được bộ thẻ. Nó cũng phơi ra dấu hiệu “sơ đồ tổ chức” (org-chart tell) ngay trên bảng, trước khi bạn có bằng chứng từ user để phản biện. | Khi nào | Làm trước card sorting, khi bạn chưa có ý kiến về cách sửa. Các thẻ sau này lấy thẳng từ danh sách này.
- Giờ: 1 phút (đề xuất)
- Ví dụ: có (slide 9, Food delivery)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Sitemap là mọi màn hình và mục user đang chạm vào hôm nay, lồng nhau từ cha đến con, đúng như sản phẩm thật.
  - Để làm gì: không viết được bộ thẻ cho nội dung chưa kiểm kê; sitemap cũng phơi ra dấu hiệu sơ đồ tổ chức trước khi có bằng chứng từ user
  - Khi nào: làm trước card sorting, khi bạn chưa có ý kiến về cách sửa
  - Nếu đã có ý kiến, bạn sẽ vẽ sitemap thiên lệch

  > **Vẽ từ sản phẩm thật, không vẽ từ trí nhớ.**
  - Đây là sitemap của sản phẩm đang chạy, không phải bản thiết kế mong muốn

  > Slide sau cho bạn xem một sitemap như vậy.

- 🎨 Visual hint: theo deck (slide 08).

---

### DIAGRAM · Minh họa · Food delivery
- Kicker: Ví dụ
- Title: Sitemap food delivery
- On-slide: Food Delivery App | Home | Search | Growth | Offers | Operations | Orders | Customer Service | Account | Current | Order detail | Track | Past | Profile | Payment | Help Centre | Order issues
- Giờ: 2 phút (đề xuất)
- Ví dụ: có (Food delivery trên slide). Cần ví dụ thật: ảnh sitemap thật đã ẩn tên của một sản phẩm bạn từng làm, đặt cạnh sơ đồ minh họa. [to confirm] ghi chú của deck nói Account (Billing) nhưng sơ đồ trên slide ghi Customer Service ở mục Account
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Khách lo vì đơn trễ. Nếu bạn là khách, bạn sẽ bấm vào đâu đầu tiên?

  - Dùng ngón tay lần theo hai đường được tô sáng, nói chậm
  - Tracking nằm ở Orders (Operations); tin nhắn "đơn trễ" nằm ở Help (Customer Service); hoàn tiền nằm ở Account
  - Rơi đúng vào giai đoạn chờ giao hàng, giai đoạn brief khoanh vùng

  > **Khách đang lo, nhưng cấu trúc lại chia nỗi lo đó cho ba team.**

  - Đây là khảo cổ, không phải phán xét; không đổ lỗi cho team nào

- 🎨 Visual hint: theo deck (slide 09).

---

### PRACTICE · Build 1
- Num: 10
- Kicker: Build 1
- Title: Vẽ sitemap inherited
- On-slide: 01 | Đặt khung: ghi câu hỏi cấu trúc và giai đoạn ở đầu trang | 02 | Đi qua và vẽ: mọi màn hình bạn chạm vào, kèm màn hình cha | 03 | Ghi owner cho từng mục cấp 1 | 04 | Khoanh dấu hiệu: những ô chỉ giải thích được bằng việc ai là owner
- Giờ: 10 phút (theo deck)
- Ví dụ: Không cần.
- Câu hỏi hay gặp:
  - Mentee làm cho sản phẩm chưa ra mắt thì sao? Cho dùng sản phẩm đối thủ.
- Speaker notes:

  > Build 1, mười phút. Mình bật timer; bạn vẽ sitemap của sản phẩm đang chạy, không vẽ từ trí nhớ.
  - Bật timer hiển thị
  - Lỗi hay gặp: vẽ theo trí nhớ, vẽ cấu trúc mong muốn, quên ghi owner
  - Nếu họ vẽ từ trí nhớ, dừng lại và mở sản phẩm thật

  > Phút 5: bạn kể lại cây từ trên xuống dưới giúp mình.

  > **Xong khi có ít nhất một ô được khoanh tròn.**

- 🎨 Visual hint: theo deck (slide 10).

---

### SECTION DIVIDER · Card Sorting
- Num: 02
- Kicker: Card Sorting
- Title: Card Sorting
- Sub: Khách hàng sẽ nhóm và đặt tên cho những gì bạn vừa vẽ ra sao.
- Giờ: 1 phút (đề xuất; cả Phần 2 là 7 phút theo deck)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Phần này dùng đúng các thẻ từ sitemap bạn vừa vẽ, nên giữ file Build 1 mở.

  - Phần 2 dài 7 phút
  - Card sort không trả lời thiết kế thế nào; nó trả lời khách nghĩ thế nào

  > **Card sort không cho bạn biết thiết kế thế nào. Nó cho bạn biết khách nghĩ thế nào.**

  > Khách hàng sẽ nhóm và đặt tên cho những gì bạn vừa vẽ ra sao?

- 🎨 Visual hint: theo deck (slide 11).

---

### COMPARE · Ba định dạng
- Kicker: So sánh
- Title: Ba định dạng card sort
- On-slide: Open | Họ tự tạo nhóm và đặt tên | Dùng khi bạn không tin cấu trúc hiện tại | Lộ ra mental model, bằng chính lời của họ | Closed | Họ sort vào nhóm của bạn | Dùng để test nhãn | Cho biết tên gọi có dễ hiểu không | Hybrid | Nhóm của bạn, cộng thêm chỗ để họ tự thêm. Dùng để tìm chỗ còn thiếu.
- Giờ: 2 phút (đề xuất)
- Ví dụ: bản nháp (app giao đồ ăn có ba nhóm Orders, Help, Account: open để khám phá nhóm, closed để test nhãn, hybrid để tìm chỗ thiếu). Cần ví dụ thật: một lần bạn chọn định dạng sort cho dự án thật và lý do
- Câu hỏi hay gặp:
  - Open sort với 5 người có đủ không? Chưa; 5 người là pilot, open sort đáng tin cần khoảng 15 (xem slide 14).
- Speaker notes:

  > Giả sử một app giao đồ ăn có sitemap ba nhóm: Orders, Help, Account. Câu hỏi của team là gì? Khách nhóm thế nào, hay tên gọi của mình có dễ hiểu không?

  - Open: họ tự tạo nhóm và đặt tên; dùng khi bạn không tin cấu trúc hiện có; lộ ra mental model bằng chính lời của họ
  - Closed: họ sort vào nhóm của bạn; là bài test nhãn, không phải test cấu trúc
  - Hybrid: nhóm của bạn cộng chỗ cho họ thêm; dùng để tìm chỗ còn thiếu, thực tế nhất khi phần lớn cây vẫn ổn
  - Phần đông senior mặc định chọn open; với dự án nhỏ, bắt đầu bằng open sort 5 người rồi quyết định

  > **Chọn định dạng theo câu hỏi bạn cần trả lời.**

  > Bạn đang cần biết nhóm, hay cần biết nhãn?

- 🎨 Visual hint: theo deck (slide 12).

---

### NUMBERED · Phương pháp · Viết thẻ
- Kicker: Cách làm
- Title: Cách viết thẻ
- On-slide: 01 | Lời của khách hàng, lấy từ JTBD map, không dùng nhãn sản phẩm | 02 | Thẻ và nhóm không dùng chung từ | 03 | Giới hạn trong một giai đoạn: 30 đến 40 thẻ | 04 | Giữ lại những thẻ khó xếp, vì đó là lý do bạn làm sort | "đồ ăn của tôi bị trễ" | "xem tài xế đang ở đâu" | "thiếu một món" | "được hoàn tiền"
- Giờ: 2 phút (đề xuất)
- Ví dụ: bản nháp (thẻ xấu: Order history, Order status, Order issues; thẻ tốt: xem lại món mình đã đặt tuần trước, đồ ăn của tôi bị trễ, thiếu một món). Cần ví dụ thật: một bộ thẻ của dự án thật, 5 thẻ trước khi sửa và 5 thẻ sau khi sửa, lấy từ lần sort gần nhất của bạn
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Ba thẻ: Order history, Order status, Order issues. Bạn sẽ xếp chúng vào nhóm nào? Cả ba vào Orders, vì trùng chữ.

  - Người sort chỉ ghép chữ, không phải suy nghĩ
  - Ý 02 là chỗ làm hỏng nhiều bài sort nhất: thẻ và nhóm không được dùng chung từ
  - Thẻ viết bằng lời của khách hàng, lấy từ JTBD map, không dùng nhãn sản phẩm; so với nhãn trong cây ở slide sitemap
  - Giới hạn trong một giai đoạn, 30 đến 40 thẻ; mệt là có thật, 90 thẻ gây nhiễu sau thẻ thứ 40
  - Giữ lại những thẻ khó xếp, vì đó là lý do bạn làm sort

  > **Thẻ viết dở thì kết quả sort chỉ phản chiếu nhãn của bạn.**

  > Chọn một thẻ xấu trong bộ của bạn và sửa ngay bây giờ, ví dụ "Order history" thành "xem lại món mình đã đặt tuần trước".

- 🎨 Visual hint: theo deck (slide 13).

---

### DIAGRAM · Minh họa · Đọc kết quả
- Kicker: Đọc kết quả
- Title: Agreement và divergence
- On-slide: Agreement | "Nó đang ở đâu" | trễ | vị trí tài xế | ETA | Divergence | "thiếu một món" | Orders | Account | Help | 5 = pilot · ~15 = open sort đáng tin
- Giờ: 1 phút (đề xuất)
- Ví dụ: có minh họa trên slide; bản nháp (15 người sort thẻ "đồ ăn của tôi bị trễ": 9 vào "Nó đang ở đâu", 4 vào "Hỗ trợ", 2 vào "Đơn hàng"). Cần ví dụ thật: một ma trận similarity hoặc bảng kết quả thật từ công cụ card sort hay bảng tính, thay cho minh họa
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Mười lăm người sort thẻ "đồ ăn của tôi bị trễ": chín người xếp vào "Nó đang ở đâu", bốn vào "Hỗ trợ", hai vào "Đơn hàng". Đây là số minh họa.

  - Chín người đồng ý là nhóm rõ (agreement), kèm tên nhóm họ đặt
  - Sáu người còn lại cho biết thẻ này cần tìm được từ ba chỗ
  - Divergence cũng là dữ liệu: thẻ bị rải ra nhiều nhóm nghĩa là khách muốn tìm nó từ nhiều chỗ, không phải khách sort sai

  > **Agreement cho bạn biết các nhóm. Divergence cho bạn biết vấn đề nằm ở đâu.**

  > Mỗi lần báo kết quả, bạn nói cỡ mẫu ngay câu đầu: 5 người là pilot, khoảng 15 mới đáng tin với open sort.

- 🎨 Visual hint: theo deck (slide 14).

---

### IMAGE · Thực tế · ReferPlus 2019
- Kicker: Thực tế · ReferPlus 2019
- Title: Card sort hai nhóm user
- On-slide: Hai nhóm user là recruiter và headhunter, dùng chung một sản phẩm | Cách làm: gặp trực tiếp, dùng whiteboard, với team nội bộ | Đầu ra: cấu trúc navigation và sitemap
- Giờ: 1 phút (đề xuất)
- Ví dụ: có (ReferPlus 2019, trên slide). Chuẩn bị ba câu: vì sao chọn whiteboard, điều gì bất ngờ nhất, điều gì sẽ làm lại nếu có thêm thời gian
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là một bài card sort mình làm năm 2019 cho ReferPlus, một sản phẩm có hai nhóm user là recruiter và headhunter.

  - Làm trực tiếp trên whiteboard, với team nội bộ
  - Đầu ra là cấu trúc navigation và sitemap
  - Đây là phương pháp tốt, nhưng người tham gia là nội bộ nên chỉ phản ánh giả định của team

  > **Bài sort này cho thấy phương pháp và giả định của team, chưa phải bằng chứng người dùng.**

  > Cần thêm gì để gọi nó là evidence-based?

  - Đáp án mong đợi: cùng bài sort với recruiter và headhunter thật, rồi tree test

- 🎨 Visual hint: theo deck (slide 15).

---

### PRACTICE · Build 2
- Num: 9
- Kicker: Build 2
- Title: Viết thẻ và sort thử
- On-slide: 01 | Viết 15 đến 20 thẻ từ sitemap, bằng ngôn ngữ JTBD | 02 | Chọn định dạng và nói rõ lý do | 03 | Pilot: mình vừa sort vừa nói to, bạn ghi lại mọi chỗ mình ngập ngừng | 04 | Sửa hai thẻ tệ nhất
- Giờ: 9 phút (theo deck: 4 viết, 1 chọn, 3 pilot, 1 sửa)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Build 2, chín phút: bốn phút viết thẻ, một phút chọn định dạng, ba phút pilot, một phút sửa.

  - Chín phút rất chặt; bật timer
  - Kiểm tra từng thẻ với cây xem có trùng từ không, trước khi pilot
  - Khi pilot, mình sort thành tiếng và cố tình ngập ngừng ở hai thẻ để bạn thấy thẻ nào có vấn đề
  - Mentee nhìn vào thẻ, không nhìn cách mình nhóm; chỉ ghi chép, không giải thích thẻ

  > **Bạn ghi lại mọi chỗ mình ngập ngừng, và không giải thích thẻ.**

  > Sửa hai thẻ tệ nhất trước khi sang phần tiếp theo.

- 🎨 Visual hint: theo deck (slide 16).

---

### SECTION DIVIDER · Tree Testing
- Num: 03
- Kicker: Tree Testing
- Title: Tree Testing
- Sub: Bước biến giả thuyết về sitemap thành bằng chứng.
- Giờ: 1 phút (đề xuất; cả Phần 3 là 7 phút theo deck)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Card sort cho biết họ sẽ nhóm thế nào. Tree test cho biết họ có tìm được không.

  - Card sort tạo cấu trúc, tree test kiểm tra cấu trúc
  - Hai bài test dùng chung một bộ nhãn nên làm liên tiếp
  - Phần 3 dài 7 phút

  > **Tree test là bước biến giả thuyết về sitemap thành bằng chứng.**

- 🎨 Visual hint: theo deck (slide 17).

---

### PROCESS · Phương pháp · Tree testing
- Kicker: Định nghĩa
- Title: Tree Testing là gì?
- On-slide: 01 | Dựng cây dưới dạng text | 02 | Viết task theo tình huống, dùng từ không xuất hiện trong cây | 03 | Đặt đích đúng cho từng task | 04 | Người tham gia click xuống chỗ họ nghĩ sẽ tìm thấy | "Đồ ăn của bạn lẽ ra đã tới từ 20 phút trước, mà bản đồ vẫn đứng yên. Bạn sẽ vào đâu để biết chuyện gì đang xảy ra?"
- Giờ: 2 phút (đề xuất)
- Ví dụ: bản nháp (task "đồ ăn lẽ ra đã tới 20 phút trước, bản đồ vẫn đứng yên"; đích đúng Orders > Đơn đang giao). Cần ví dụ thật: mở một tree test thật trên màn hình bằng công cụ tree test, cho mentee thử làm một task trong 30 giây
- Câu hỏi hay gặp:
  - Cần bao nhiêu task? Khoảng 10, nhắm vào phần muốn cải thiện, mỗi task dưới 30 giây.
- Speaker notes:

  > "Đồ ăn của bạn lẽ ra đã tới từ 20 phút trước, mà bản đồ vẫn đứng yên. Bạn sẽ vào đâu để biết chuyện gì đang xảy ra?"

  - Đích đúng của task này là Orders > Đơn đang giao
  - Task không được chứa chữ có trong cây; từ cần tránh: order, track, status, help
  - Lỗi phổ biến: task viết bằng đúng chữ trong cây khiến người tham gia chỉ khớp chữ
  - Bỏ giao diện là chủ ý: loại màu, icon, layout đang che lỗi của nhãn, chỉ test nhãn và phân cấp
  - Bốn bước: dựng cây dạng text, viết tình huống bằng từ không có trong cây, đặt đích đúng, người tham gia click xuống nơi họ sẽ tìm
  - Viết thêm hai task tương tự: thiếu món, và xin hoàn tiền

  > **Task phải dùng từ của khách, không dùng từ có trong cây.**

  > Task vừa rồi tránh những từ nào?

- 🎨 Visual hint: theo deck (slide 18).

---

### DIAGRAM · Đọc kết quả
- Kicker: Đọc kết quả
- Title: Success, directness, first click
- On-slide: 01 | Success | Tới được đích đúng | 02 | Directness | Đi thẳng tới nơi, không quay lại | 03 | First click | Mục họ thử đầu tiên | Kém <40% | Tạm 41–60% | Khá 61–80% | ▼ median 62% | Tốt 80–90% | Xuất sắc >90% | Median qua 98 nghiên cứu: 62% (Albert & Tullis, qua NN/g)
- Giờ: 2 phút (đề xuất)
- Ví dụ: bản nháp (success 48%, directness 35%, first click chia Orders 52% và Account 48%). Cần ví dụ thật: một báo cáo tree test thật, đã ẩn thông tin, để mentee thấy bảng success, directness, first click. [to confirm] nguồn median 62% và ngưỡng (Albert & Tullis, qua NN/g) chưa được kiểm tra lại
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Success 48 phần trăm, directness 35 phần trăm, first click chia gần đôi giữa Orders và Account. Bạn đọc ra điều gì, và sẽ nói gì với stakeholder?

  - Success là tới được đích đúng; directness là đi thẳng, không quay lại; first click là mục họ thử đầu tiên
  - Success cao nhưng directness thấp nghĩa là tới được nhưng phải đi vòng: cấu trúc dùng được nhưng chưa tốt
  - First click là chỉ số nên theo dõi nhất vì nó cho thấy trực giác đầu tiên
  - Ngưỡng tham khảo: dưới 40% kém, 80 đến 90% tốt, trên 90% xuất sắc; median 62% qua 98 nghiên cứu (Albert & Tullis, qua NN/g)
  - Task sống còn cần trên 90%; "đồ ăn có đến không" là một task sống còn
  - So sánh hai cây cần mẫu lớn, khoảng 50 người mỗi cây; đừng để pilot giả làm bằng chứng

  > **Hơn một nửa khách hàng không tìm ra đơn hàng ở lần thử đầu tiên, và những người tìm ra thì đi vòng.**

  > Task sống còn của sản phẩm bạn là task nào?

- 🎨 Visual hint: theo deck (slide 19).

---

### DIAGRAM · Minh họa · Food delivery
- Kicker: Ví dụ
- Title: Kết quả tree test
- On-slide: 48% | Success · Directness: thấp | First click | Orders | 52% | Account | 48%
- Giờ: 1 phút (đề xuất)
- Ví dụ: có minh họa trên slide
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Bốn mươi tám phần trăm tìm ra đơn hàng, và first click chia đôi: Orders 52 phần trăm, Account 48 phần trăm. Đây là số liệu minh họa.

  - Người dùng chia làm hai phe, nghĩa là một nửa khách hàng tìm đơn hàng ở sai chỗ
  - Đây chính là dấu hiệu sơ đồ tổ chức, dưới dạng con số mà stakeholder đọc được
  - Ranh giới Operations và Customer Service chính là ranh giới ở slide sitemap

  > **Một nửa khách hàng tìm đơn hàng ở sai chỗ.**

  > Số liệu thật của bạn đến từ bài tập sau buổi này.

- 🎨 Visual hint: theo deck (slide 20).

---

### IMAGE · Thực tế · ReferPlus 2019
- Kicker: Thực tế · ReferPlus 2019
- Title: Sitemap dựng lại
- On-slide: Mobile IA v0.2: phân cấp màn hình, không phải wireframe | Xây từ: kết quả card sort và journey mapping | Để ý: có hai đường vào, mỗi nhóm user một đường, rồi nhập lại ở các màn hình chung
- Giờ: 1 phút (đề xuất)
- Ví dụ: có (ReferPlus 2019, trên slide). Chuẩn bị số liệu trước và sau nếu có: số bước, tỉ lệ hoàn thành, hoặc phản hồi của stakeholder
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là sitemap ReferPlus sau khi mình dựng lại quanh việc của người dùng.

  - Đây là Mobile IA v0.2: phân cấp màn hình, không phải wireframe
  - Xây từ kết quả card sort và journey mapping
  - Chỉ vào chỗ hai đường vào, mỗi nhóm user một đường, rồi nhập lại ở các màn hình chung
  - Nối lại với khoảng trống ở slide đọc kết quả card sort

  > **Tổ chức quanh việc của người dùng, không quanh quyền sở hữu tính năng, trông như thế này trên giấy.**

  > Nếu tree test cấu trúc này, bạn sẽ viết task nào? Gợi ý: một task cho recruiter, một task cho headhunter.

- 🎨 Visual hint: theo deck (slide 21).

---

### PRACTICE · Build 3
- Num: 8
- Kicker: Build 3
- Title: Đặt cược và thiết kế test
- On-slide: 01 | Chỉ vẽ lại phần của cây mà đáp án của bạn thay đổi | 02 | Gắn nhãn: "Giả thuyết, chưa được test" | 03 | Viết ba task kèm đích đúng | 04 | Đặt kill threshold: tỉ lệ success thấp tới mức bạn sẽ bỏ phương án này
- Giờ: 8 phút (theo deck: 4 vẽ lại, 3 task, 1 ngưỡng)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Build 3, tám phút: bốn phút vẽ lại cây, ba phút viết task, một phút đặt ngưỡng.

  - Đáp án lấy từ danh sách năm cách ở slide 3
  - Chọn theo giả thuyết dễ test nhất, không chọn theo cảm tính
  - Chỉ vẽ lại phần của cây mà đáp án thay đổi, gắn nhãn "Giả thuyết, chưa được test"
  - Đầu ra điền vào ia-decision-record.md, phần 1 đến 3
  - Ví dụ ngưỡng: success dưới 60% thì bỏ phương án; viết ra trước khi test, không điều chỉnh sau

  > **Chiêu của senior: quyết định trước điều gì sẽ chứng minh mình sai.**

  > Viết ngưỡng bỏ phương án của bạn ngay bây giờ.

- 🎨 Visual hint: theo deck (slide 22).

---

### SECTION DIVIDER · User Flows
- Num: 04
- Kicker: User Flows
- Title: User Flows
- Sub: Màn hình đẹp nằm trong flow sai thì vẫn là thiết kế hỏng.
- Giờ: 1 phút (đề xuất; cả Phần 4 là 8 phút, nâng từ 6 phút của deck)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Hôm nay luồng chỉ có một việc: cho thấy cấu trúc hiện tại tốn gì ở một task cốt lõi, như "xem đơn đang giao".

  - Phần 4 giữ gọn, vì mentee đã học flow ở buổi khác
  - Mục tiêu duy nhất là dùng flow để đo cái giá của cấu trúc

  > **Màn hình đẹp nằm trong flow sai thì vẫn là thiết kế hỏng.**

- 🎨 Visual hint: theo deck (slide 23).

---

### NUMBERED · USER FLOW
- Kicker: Định nghĩa
- Title: User Flow là gì?
- On-slide: Là gì | Sơ đồ các bước một user đi qua để hoàn thành một task cụ thể, từ điểm vào đến kết quả cuối. | Không phải wireframe. Đây là bản đồ màn hình, hành động và quyết định trên đường đi của task, nhìn từ phía user. | Mục tiêu | Thiết kế và kiểm tra đường đi của task trước khi vẽ màn hình nào. Tìm friction và state còn thiếu khi sửa vẫn còn rẻ. | Khi nào dùng | Trước khi wireframe: chốt cấu trúc của task trước khi thiết kế màn hình | Rà soát sản phẩm cũ: ghi lại những gì user thật sự phải làm | Tìm friction: chỗ user bỏ đi hoặc bị lạc | Bàn giao màn hình cho engineering: cho thấy mỗi màn hình xuất hiện khi nào và trong điều kiện nào
- Giờ: 1 phút (đề xuất)
- Ví dụ: bản nháp (flow "Đặt và xác nhận một slot": sáu bước và hai điểm quyết định, ở slide 28). Cần ví dụ thật: một user flow thật từ dự án của bạn (onboarding hoặc checkout), đã ẩn thông tin, để mentee so với định nghĩa
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Một user flow cho task "Đặt và xác nhận một slot" không vẽ mười màn hình. Nó chỉ vẽ sáu bước và hai điểm quyết định.

  - Nói sớm: user flow không phải wireframe, vì nhiều người vẽ hộp màn hình rồi gọi là flow
  - Nhấn vào "một người, một task"
  - Mục tiêu là tìm ma sát và state còn thiếu khi sửa vẫn còn rẻ
  - Dùng khi: trước wireframe, rà soát sản phẩm cũ, tìm chỗ user rơi rụng, bàn giao cho engineering

  > **Một user, một task, từ điểm vào đến kết quả.**

  > Flow trong dự án của bạn có đúng là một người, một task không?

- 🎨 Visual hint: theo deck (slide 24).

---

### COMPARE · User Flow · Phạm vi
- Kicker: Phạm vi
- Title: Phạm vi của user flow
- On-slide: Trong phạm vi | Một user, một task, một điểm vào | Màn hình, hành động, quyết định | Những gì user nhìn thấy | Ngoài phạm vi | Các actor khác (admin, support, payment provider) | Việc hệ thống làm phía sau | Bàn giao nội bộ → Process Map | Khi không có user flow | Bạn thiết kế màn hình mà không biết trước và sau nó là gì | State lỗi và edge case chỉ lộ ra khi dev, không phải khi thiết kế | Stakeholder tranh luận chi tiết màn hình khi chưa thống nhất cấu trúc của task
- Giờ: 1 phút (đề xuất)
- Ví dụ: cần ví dụ: một dự án thật nơi state lỗi hoặc edge case chỉ lộ ra khi dev, vì thiếu user flow
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Nếu task có một actor thứ hai, như admin, support hay payment provider, bạn đã sang process map.

  - Trong phạm vi: một user, một task, một điểm vào; màn hình, hành động, quyết định; điều user nhìn thấy
  - Ngoài phạm vi: actor khác; việc hệ thống làm phía sau; bàn giao nội bộ
  - Ba cái giá khi bỏ qua flow: thiết kế màn hình mà không biết trước và sau nó là gì; state lỗi và edge case lộ ra khi dev; stakeholder cãi chi tiết màn hình khi chưa thống nhất cấu trúc của task
  - Giữ phạm vi này giúp flow dễ đọc

  > **Phần lớn vấn đề thiết kế nằm ở flow, không nằm ở màn hình.**

- 🎨 Visual hint: theo deck (slide 25).

---

### PROCESS · Phương pháp · Vẽ flow
- Kicker: Cách làm
- Title: Cách vẽ một user flow
- On-slide: 01 | Đặt tên task | Đặt tên cho cụ thể. Không phải “checkout”, mà là “Đặt và xác nhận một slot (user đã dùng app trước đó)”. | 02 | Xác định điểm vào và điểm kết thúc | Vẽ pill Start và End trước mọi thứ khác. | 03 | Vẽ happy path trước | Chuỗi bước lý tưởng khi mọi thứ đều suôn sẻ. | 04 | Thêm nhánh lỗi và edge case | Slot đã bị lấy, chưa đăng nhập, empty state. Mỗi nhánh đều phải có đích. | 05 | Ghi chú ở chỗ có friction | Đánh dấu bước đó, ghi rõ nó tốn gì. | 06 | Kiểm tra độ đầy đủ | Mỗi diamond có hai mũi tên ra, đều có nhãn. Không để hình nào bị bỏ lẻ.
- Giờ: 1 phút (đề xuất)
- Ví dụ: có (tên task trên slide: "Đặt và xác nhận một slot", không phải "checkout")
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Không phải "checkout". Mà là "đặt và xác nhận một slot, user đã dùng app trước đó".

  - Sáu bước, happy path trước; đi chậm, ưu tiên bước 01 và 04
  - 01 đặt tên task cụ thể để flow không quá rộng; 02 vẽ Start và End trước; 03 vẽ happy path
  - 04 thêm nhánh lỗi và edge case; đây là nơi lộ state còn thiếu
  - 05 ghi chú chỗ có ma sát, và ghi rõ nó tốn gì
  - 06 kiểm tra: mỗi diamond có hai mũi tên có nhãn, không có hình mồ côi

  > **Mỗi nhánh phải có đích. Không để mũi tên treo.**

- 🎨 Visual hint: theo deck (slide 26).

---

### DIAGRAM · Cấu tạo · User flow
- Kicker: Cấu tạo
- Title: 5 hình của user flow
- On-slide: Pill | Điểm bắt đầu và kết thúc | “User mở app” | “Đã xác nhận đặt chỗ” | Rectangle | Một màn hình hoặc hành động của user | Xem danh sách slot | Bấm “Pay” | Diamond | Điểm quyết định | “Slot còn trống không?” | “Thanh toán thành công?” | Arrow | Hướng đi của flow | Gắn nhãn cho nhánh: | Yes / No, Success / Error | friction | Note | Ngữ cảnh không nhét vừa một hình | “Friction: phải bấm 3 lần mới tới đây” | Dùng hình nhất quán thì ai trong team cũng đọc được flow của bạn. Nếu cần hình thứ sáu, thường đó là một bước của hệ thống, tức là chuyện của Process Map.
- Giờ: 1 phút (theo deck: 60 giây cho người đã senior)
- Ví dụ: có (nhãn mẫu trên slide: "Slot còn trống không?", "Thanh toán thành công?")
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Năm hình mang toàn bộ ý nghĩa. Mình đi qua trong sáu mươi giây.

  - Pill là điểm bắt đầu và kết thúc; Rectangle là màn hình hoặc hành động; Diamond là điểm quyết định; Arrow là hướng đi; Note là ngữ cảnh không nhét vừa một hình
  - Nhấn quy tắc diamond: đúng hai mũi tên ra, đều có nhãn như Yes và No
  - Dùng hình nhất quán thì cả team đọc được flow mà không cần giải thích

  > **Nếu cần hình thứ sáu, đó thường là một bước của hệ thống, tức là chuyện của process map.**

- 🎨 Visual hint: theo deck (slide 27).

---

### DIAGRAM · Ví dụ · Đặt và xác nhận một slot
- Kicker: Ví dụ
- Title: Đặt và xác nhận một slot
- On-slide: Start | → | Xem danh sách slot | → | Chọn slot | → | Slot còn trống? | → | Yes | Xem lại đặt chỗ | ↓ | Thanh toán | ← | Thanh toán OK? | ← | Yes | Đã xác nhận đặt chỗ | ← | End | No | Quay lại danh sách slot | No | Lỗi: thử lại hoặc đổi phương thức | Màn hình xác nhận hiện “pending”, không phải “confirmed”. | Flow chỉ cho thấy những gì user thấy, nên không giải thích được vì sao lại hiện “pending”. → phần tiếp theo.
- Giờ: 1 phút (đề xuất)
- Ví dụ: có minh họa trên slide. Bản nháp (đáp án gợi ý cho "pending": đơn vượt hạn mức tự duyệt và đang chờ Ops team). Cần ví dụ thật: một flow thật có bước "pending", như chuyển khoản hoặc duyệt đơn
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Ở bước cuối, màn hình xác nhận hiện "pending", không phải "confirmed". Tại sao lại là pending?

  - Đi từ trái sang phải, rồi xuống và quay ngược ở hàng hai
  - Dừng ở diamond "Slot còn trống?" và nhánh lỗi thanh toán
  - Để mentee đoán trước khi sang phần Process Map; dừng năm giây im lặng sau câu hỏi
  - Gợi ý đáp án: đơn vượt hạn mức tự duyệt và đang chờ Ops team; màn hình không có lỗi, quy trình phía sau mới là nguyên nhân

  > **Flow chỉ cho thấy những gì user thấy, nên không giải thích được vì sao hiện "pending".**

  > Câu trả lời nằm ở phần Process Map.

- 🎨 Visual hint: theo deck (slide 28).

---

### NUMBERED · Một flow tốt cho bạn thấy gì
- Kicker: Đọc flow
- Title: Ba điều flow cho bạn thấy
- On-slide: 01 | Điểm quyết định bắt user làm việc mà hệ thống có thể tự xử lý | 02 | Flow dài hơn mức cần thiết vì nội dung nằm sai chỗ trong IA | 03 | Thiếu state: empty, error, loading, success | 7 | Task cốt lõi mà dài hơn 7 bước thì nhiều khả năng lỗi nằm ở IA, không phải ở thiết kế màn hình.
- Giờ: 1 phút (đề xuất)
- Ví dụ: cần ví dụ: một flow thật dài hơn bảy bước mà nguyên nhân nằm ở IA, không nằm ở màn hình
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Task cốt lõi của bạn có bao nhiêu bước?

  - Ba điều cần tìm trong một flow
  - 01 quyết định mà user phải làm thay việc hệ thống có thể tự xử lý
  - 02 flow dài hơn mức cần thiết vì nội dung nằm sai chỗ trong IA
  - 03 thiếu state: empty, error, loading, success

  > **Task cốt lõi mà dài hơn bảy bước thì nhiều khả năng lỗi nằm ở IA, không phải ở thiết kế màn hình.**

- 🎨 Visual hint: theo deck (slide 29).

---

### COMPARE · JTBD → Flow
- Kicker: JTBD → Flow
- Title: Đánh giá flow bằng JTBD Map
- On-slide: Với mỗi bước, hãy hỏi: bước này giúp user tiến gần job của họ, hay chỉ là friction do hệ thống tự tạo ra? | JTBD insight | Hệ quả cho flow | User cần xác nhận nhanh trước khi mất slot | → | Không đặt màn hình upsell trên đường đi chính | User lo lắng về những hành động không thể hoàn tác | → | Thêm bước review trước khi xác nhận cuối cùng | User muốn trông chuyên nghiệp khi chia sẻ sản phẩm của mình | → | Đặt “share” ngay lúc hoàn thành task, đừng giấu trong settings
- Giờ: 1 phút (đề xuất)
- Ví dụ: bản nháp (job "tôi muốn biết đơn có tới kịp trước 7 giờ không" dẫn tới hiển thị giờ dự kiến ở màn hình đầu tiên). Cần ví dụ thật: JTBD map thật của mentee hoặc của bạn, không dùng ví dụ trên slide
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Job: "Tôi muốn biết đơn có tới kịp trước 7 giờ không." Hệ quả cho flow: hiển thị giờ dự kiến ở màn hình đầu tiên, không cần bấm vào từng đơn.

  - Dùng JTBD map từ buổi trước
  - Mỗi bước hỏi: bước này giúp user tiến tới job, hay chỉ là ma sát do hệ thống tự tạo
  - Ví dụ trên slide: cần xác nhận nhanh thì không đặt upsell ở đường chính; lo việc không thể hoàn tác thì thêm bước review; muốn tỏ ra giỏi khi chia sẻ thì đưa "share" ra lúc hoàn thành

  > **Mỗi cặp nhu cầu của user và hệ quả cho flow là một quyết định thiết kế.**

  > Lấy một job từ JTBD map của bạn và điền hệ quả cho flow ngay bây giờ.

- 🎨 Visual hint: theo deck (slide 30).

---

### PRACTICE · Hoạt động 1
- Num: 20
- Kicker: Hoạt động 1
- Title: Vẽ user flow
- On-slide: Công cụ · FigJam hoặc Miro | Bắt đầu từ happy path | Ví dụ đầu ra · Hoạt động 1 | user-flow | · Đặt và xác nhận một slot | Draft | Start | → | Xem danh sách slot | → | Chọn slot | → | Slot còn trống? | Lỗi: quay lại danh sách | Ghi chú: phải bấm 3 lần mới tới đây | Ví dụ giả định. Task, các bước và số bước của bạn sẽ khác. | Các bước của bạn | Chọn một dự án thật | Chọn task cốt lõi mà user cần hoàn thành | Đi qua từng màn hình, vẽ mỗi bước bằng 5 hình | Happy path trước, rồi thêm một nhánh lỗi và một ghi chú
- Giờ: 20 phút (theo deck)
- Ví dụ: có (ví dụ đầu ra giả định trên slide: "Đặt và xác nhận một slot")
- Câu hỏi hay gặp:
  - Hết giờ mà chưa có nhánh lỗi thì sao? Thêm ba phút rồi dừng, không kéo dài.
- Speaker notes:

  > Hoạt động 1, hai mươi phút: chọn một dự án thật, một task cốt lõi, và vẽ flow bằng năm hình.

  - Bật timer; công cụ là FigJam hoặc Miro
  - Tự đi qua từng màn hình, happy path trước, rồi thêm một nhánh lỗi và một note
  - Lỗi hay gặp: chọn task quá rộng như "mua hàng", hoặc vẽ cả màn hình

  > **Phút 10: chưa có diamond nghĩa là bạn đang vẽ danh sách, không phải flow.**

- 🎨 Visual hint: theo deck (slide 31).

---

### SECTION DIVIDER · Process Map
- Num: 05
- Kicker: Process Map
- Title: Process Map
- Sub: Lùi ra xa để thấy ai làm gì phía sau màn hình, và việc đang kẹt ở đâu.
- Giờ: 1 phút (đề xuất; cả Phần 5 là 9 phút, nâng từ 6 phút của deck)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Nếu cùng một task, ai khác ngoài user đang làm việc? Hãy kể ba đến bốn actor.

  - Để mentee kể đủ ba đến bốn actor trước khi sang slide tiếp theo
  - Process map là cùng một task với user flow, thu nhỏ lại để nhìn toàn cảnh

  > **Ai làm gì phía sau màn hình, và công việc chờ ở đâu?**

- 🎨 Visual hint: theo deck (slide 32).

---

### NUMBERED · Định nghĩa · Process Map
- Kicker: Định nghĩa
- Title: Process Map là gì?
- On-slide: Là gì | Sơ đồ cho thấy công việc chuyển qua lại giữa các actor (user, hệ thống, team nội bộ và bên thứ ba) để ra được một kết quả. | User flow đi theo đường của một người. Process map cho thấy toàn bộ vận hành phía sau, kể cả phần user không bao giờ nhìn thấy. | Mục tiêu | Nhìn rõ chỗ bàn giao (handoff), chỗ phụ thuộc lẫn nhau và chỗ nghẽn (bottleneck). Từ đó tìm ra những bước chỉ có vì cách tổ chức hoặc hệ thống được dựng, chứ user không hề cần. | Khi nào dùng | Có hơn một actor: checkout qua payment provider, onboarding có email hệ thống, tính năng admin | User flow trông ổn nhưng user vẫn bị delay hoặc bối rối, và màn hình không giải thích được | Trước khi bàn giao cho engineering: cho thấy logic back-stage phía sau mỗi màn hình | Thống nhất giữa design, engineering và operations về việc ai chịu trách nhiệm bước nào
- Giờ: 1 phút (đề xuất)
- Ví dụ: bản nháp (khách bấm "Hoàn tiền" và thấy "Đang xử lý" suốt ba ngày; bốn lane User, System, Support, Finance). Cần ví dụ thật: một ví dụ thật nơi user thấy "chờ duyệt" còn nguyên nhân nằm ở team vận hành, như duyệt hoàn tiền hoặc duyệt tài khoản
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Khách bấm "Hoàn tiền" và thấy "Đang xử lý" suốt ba ngày. User flow chỉ có ba bước. Vậy đơn đang nằm ở đâu?

  - Process map có bốn lane: User, System, Support, Finance, và đơn nằm chờ ở lane Finance
  - User flow đi theo một người; process map cho thấy cả vận hành, kể cả phần user không nhìn thấy
  - Mục tiêu là lộ ra handoff, phụ thuộc, nút thắt cổ chai, và tìm bước tồn tại vì cách tổ chức hoặc hệ thống được xây, không vì user cần
  - Dùng khi: nhiều actor; flow ổn mà user vẫn bị trễ hoặc bối rối; trước khi giao cho engineering; căn chỉnh design, engineering và ops
  - Process map không thay thế user flow, nó đặt flow vào bối cảnh; ghi lên bảng: handoff, phụ thuộc, bottleneck

  > **Màn hình không sai. Quy trình mới sai.**

- 🎨 Visual hint: theo deck (slide 33).

---

### COMPARE · Process Map · Phạm vi
- Kicker: Phạm vi
- Title: Phạm vi của process map
- On-slide: Trong phạm vi | Nhiều actor | Front-stage và back-stage | Từ đầu đến cuối, từ trigger đến kết quả | Ngoài phạm vi | Layout và chi tiết màn hình | Cảm xúc và quyết định của một user | Cùng task. Cùng flow. Khung nhìn rộng hơn.
- Giờ: 1 phút (đề xuất)
- Ví dụ: có (nối với ví dụ hoàn tiền ở slide 33)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Ở ví dụ hoàn tiền, process map bàn về điều gì, và không bàn về điều gì?

  - Trong phạm vi: nhiều actor; front-stage và back-stage; từ trigger đến kết quả
  - Ngoài phạm vi: layout và chi tiết màn hình; cảm xúc và quyết định của một user
  - Hai thứ ngoài phạm vi vẫn thuộc user flow; process map không thay thế chúng
  - Giữ phạm vi này giúp map dễ đọc: nếu map bắt đầu bàn về màn hình, bạn đang lẫn với flow

  > **Cùng task, cùng flow, khung nhìn rộng hơn.**

- 🎨 Visual hint: theo deck (slide 34).

---

### PROCESS · Phương pháp · Dựng map
- Kicker: Cách làm
- Title: Cách dựng một process map
- On-slide: 01 | Bắt đầu từ user flow | Các bước của nó trở thành lớp front-stage. | 02 | Liệt kê các actor | User, hệ thống, team nội bộ, bên thứ ba. Mỗi actor một swimlane. | 03 | Đặt mỗi bước vào lane của người sở hữu | Kể cả những bước user không bao giờ thấy. | 04 | Đánh dấu các handoff | Mỗi mũi tên băng qua một lane. Ghi rõ thứ được chuyển đi. | 05 | Tìm các bước chờ, lặp, mồ côi | Bất cứ chỗ nào công việc bị kẹt hoặc lặp vòng. | 06 | So với user flow | Bước nào user chỉ cảm nhận được dưới dạng độ trễ?
- Giờ: 1 phút (đề xuất)
- Ví dụ: cần ví dụ: một process map thật của một dự án, có các handoff được đánh dấu
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Bắt đầu từ user flow bạn vừa vẽ: các bước của nó trở thành lớp front-stage.

  - 01 bắt đầu từ flow; 02 liệt kê actor, mỗi actor một swimlane
  - 03 đặt mỗi bước vào lane của người sở hữu, kể cả bước user không bao giờ thấy
  - 04 đánh dấu handoff: mỗi mũi tên băng qua lane, ghi rõ thứ được chuyển đi
  - 05 tìm chỗ chờ, lặp, mồ côi
  - 06 so với user flow để thấy bước nào user chỉ cảm nhận như độ trễ; đây là điểm ăn tiền

  > **Mỗi mũi tên băng qua lane là một nguy cơ trễ.**

  > Bước nào trong flow của bạn mà user chỉ cảm nhận như độ trễ?

- 🎨 Visual hint: theo deck (slide 35).

---

### DIAGRAM · Cấu tạo · Process map
- Kicker: Cấu tạo
- Title: Hình và công cụ process map
- On-slide: Swimlane | Mỗi lane một actor | User · System | Ops team · Payment provider | Rectangle | Một hành động của actor đó | Ops team review đặt chỗ | Diamond | Điểm quyết định | “Vượt hạn mức tự động duyệt?” | Parallelogram | Bước tự động của hệ thống | Khóa slot, gửi email, kiểm tra thẻ | Handoff arrow | Công việc băng qua các lane | System → Ops team: | “cần duyệt”
- Giờ: 1 phút (đề xuất)
- Ví dụ: có (nhãn mẫu trên slide: khóa slot, gửi email, kiểm tra thẻ, Ops team review đặt chỗ)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Hãy tự phân loại ba hành động: gửi email xác nhận, Ops review đơn, kiểm tra thẻ. Hành động nào là hình gì?

  - Hai thứ mới so với user flow: hình bình hành là bước tự động của hệ thống, và mũi tên handoff
  - Swimlane là khung chứa mọi thứ: mỗi lane một actor
  - Rectangle là hành động của actor đó; Diamond là quyết định, ví dụ vượt hạn mức tự duyệt hay không
  - Đáp án: gửi email xác nhận và kiểm tra thẻ là hình bình hành; Ops review đơn là hình chữ nhật trong lane Ops

  > **Hai thứ mới: hình bình hành cho bước tự động, và mũi tên handoff.**

- 🎨 Visual hint: theo deck (slide 36).

---

### DIAGRAM · Ví dụ · Đặt và xác nhận một slot
- Kicker: Ví dụ
- Title: Cùng task, bốn lane
- On-slide: User | Chọn slot | Thanh toán | user chờ | Thấy “pending” | System | Khóa slot | Yêu cầu thanh toán | Gắn cờ: cần duyệt | Ops team | Vượt hạn mức tự động duyệt? | No | Duyệt thủ công | 3rd party | Gateway trả kết quả | “Pending” không phải lỗi màn hình. | Đó là một handoff thủ công mà user không bao giờ thấy. Cách sửa nằm ở quy trình: tự động duyệt dưới một hạn mức, hiển thị trạng thái duyệt.
- Giờ: 1 phút (đề xuất)
- Ví dụ: có minh họa trên slide. Cần ví dụ thật: process map thật của dự án, thay vào hoặc đặt cạnh bên
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Nhớ màn hình xác nhận hiện "pending" ở user flow chứ? Đây là lý do: đó không phải lỗi màn hình, đó là một handoff thủ công mà user không bao giờ thấy.

  - Cùng task, bốn lane: User, System, Ops team, 3rd party
  - Dùng ngón tay lần theo handoff từ System sang Ops team
  - Lane User yên lặng trong khi lane Ops bận; đó là chỗ user thấy "pending"
  - Cách sửa nằm ở quy trình: tự duyệt dưới một hạn mức và hiển thị trạng thái duyệt, không chỉnh màn hình

  > **Cách sửa nằm ở quy trình, không nằm ở màn hình.**

  > Nếu tự động duyệt dưới 5 triệu đồng, bao nhiêu phần trăm đơn không phải chờ?

- 🎨 Visual hint: theo deck (slide 37).

---

### IMAGE · Thực tế · Process flow diagram
- Kicker: Thực tế
- Title: Lane, actor và handoff
- On-slide: Nguồn: aha.io · Process flow diagram template
- Giờ: 1 phút (đề xuất)
- Ví dụ: có (template process flow của Aha! trên slide). Cần ví dụ thật: thêm một process map từ dự án của bạn để cho thấy mức chi tiết thực tế
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là một process flow có swimlane. Trong sáu mươi giây, hãy tìm các điểm quyết định, rồi tìm chỗ đổi lane.

  - Mỗi lane là một actor, mỗi mũi tên băng qua lane là một handoff
  - Sau sáu mươi giây mới chỉ: có bao nhiêu điểm quyết định, mũi tên nào băng qua lane, bước nào user không thấy
  - Nguồn là template của Aha!, nên nói rõ đây là template tham khảo chứ không phải dự án của bạn

  > **Nhiều handoff thường nghĩa là nhiều độ trễ.**

- 🎨 Visual hint: theo deck (slide 38).

---

### COMPARE · So sánh
- Kicker: So sánh
- Title: User Flow vs Process Map
- On-slide: User Flow | Process Map | Góc nhìn | Một user | Cả tổ chức | Câu hỏi | User trải qua những gì? | Ai làm gì, và công việc chờ ở đâu? | Hiển thị | Chỉ front-stage | Front-stage và back-stage | Hình dùng | Pill, Rectangle, Diamond, Arrow, Note | + Swimlane, Parallelogram, Handoff arrow | Thứ tự | Vẽ trước | Vẽ sau, thu nhỏ khung
- Giờ: 2 phút (đề xuất; slide mang cả ví dụ đặt đồ ăn, nên tách làm hai slide trong deck)
- Ví dụ: có (ví dụ dạy: đặt một phần cơm trưa trên app giao đồ ăn, bốn lane Khách, App, Quán, Tài xế). Lưu ý: ví dụ minh họa luồng chung của dạng app này, không phải tài liệu nội bộ của một công ty cụ thể
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Task: "đặt một phần cơm trưa và biết khi nào nó tới". User flow có sáu bước: mở app, chọn quán, chọn món, thanh toán, theo dõi đơn, nhận hàng. Flow này có vấn đề gì không?

  - Mentee thường nói flow này ổn và rõ ràng
  - Process map có bốn lane: Khách, App, Quán, Tài xế
  - App ghi nhận đơn, trừ tiền, gửi đơn cho quán, tìm tài xế; quán xác nhận, nấu, đánh dấu "đã xong" mà khách không nhìn thấy
  - Tài xế nhận cuốc, tới quán, chờ món, giao; có thể phải chờ quán hoặc ghép nhiều đơn
  - Ba handoff: App sang Quán (đơn mới), Quán sang Tài xế (món xong), Tài xế sang App (đã lấy hàng, đã giao)
  - Đáp án cho câu "sửa ở màn hình hay ở quy trình": ở quy trình, bằng cách báo "quán đang chuẩn bị" và ước tính thời gian nấu, không làm đẹp màn hình theo dõi
  - So sánh hai sơ đồ: góc nhìn (một user so với cả tổ chức), câu hỏi, hiển thị (chỉ front-stage so với cả hai), hình dùng, và thứ tự (vẽ flow trước, vẽ map sau)
  - Gắn với dự án của bạn: task của bạn có actor nào mà user không bao giờ thấy? Ghi tên họ lên bảng

  > **Màn hình theo dõi chỉ đứng yên khi quán chưa bấm xong hoặc tài xế đang chờ món. Khách chỉ cảm nhận là app chậm.**

  > Sửa ở màn hình hay ở quy trình?

  > Khi nào bạn dừng ở user flow và không cần process map?

- 🎨 Visual hint: theo deck (slide 39).

---

### PRACTICE · Hoạt động 2
- Num: 15
- Kicker: Hoạt động 2
- Title: Vẽ process map
- On-slide: Đầu ra · swimlane | Các bước của bạn | Lấy lại đúng task và flow đã làm | Liệt kê các actor, mỗi actor một swimlane | Thêm các bước back-stage
- Giờ: 15 phút (theo deck)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Hoạt động 2, mười lăm phút: lấy lại đúng task và flow ở Hoạt động 1, vẽ lại thành lane.

  - Bật timer; không thêm task mới
  - Liệt kê actor, mỗi actor một swimlane, thêm các bước back-stage, đánh dấu mọi handoff
  - Khoanh những chỗ user phải chờ

  > **Phút 8: mỗi lane có ít nhất một bước chưa, và mỗi mũi tên băng lane đã có nhãn chưa?**

- 🎨 Visual hint: theo deck (slide 40).

---

### SECTION DIVIDER · Defend Your IA
- Num: 06
- Kicker: Defend Your IA
- Title: Defend Your IA
- Sub: Có bằng chứng cho thấy nên đổi, chưa chắc nó sẽ được đổi.
- Giờ: 1 phút (đề xuất; cả Phần 6 là 6 phút theo deck)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Mọi thứ đến giờ là tay nghề. Phần này là sức ảnh hưởng.

  - Phần 6 dài 6 phút; đây là nửa của senior
  - Chuyển giọng từ nghề thủ công sang ảnh hưởng
  - Các mục bạn muốn dời đang được người có lý do riêng sở hữu

  > **Có bằng chứng cho thấy nên đổi, chưa chắc nó sẽ được đổi.**

- 🎨 Visual hint: theo deck (slide 41).

---

### NUMBERED · File của bạn · ia-decision-record.md
- Kicker: File của bạn
- Title: ia-decision-record.md
- On-slide: 01 | Câu hỏi cấu trúc | 02 | Các phương án đã cân nhắc | 03 | Quyết định: trước và sau | 04 | Bằng chứng: kèm cỡ mẫu và nhãn "provisional" | 05 | Liên kết với root outcome của brief | 06 | Ai bị ảnh hưởng: các mục và owner | 07 | Điều gì sẽ khiến mình đổi ý
- Giờ: 2 phút (đề xuất)
- Ví dụ: bản nháp (câu hỏi "trạng thái đơn đang giao nên nằm ở đâu": trước Orders > Chi tiết đơn, sau Home hiển thị đơn đang giao). Cần ví dụ thật: một ia-decision-record.md mẫu đã điền, một trang, để mentee thấy mức chi tiết mong đợi
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Câu hỏi cấu trúc: "Trạng thái đơn đang giao nên nằm ở đâu?" Trước: Orders, Chi tiết đơn. Sau: Home hiển thị đơn đang giao. Bằng chứng: tree test, 15 người, gắn nhãn provisional. Sẽ đổi ý nếu success dưới 60 phần trăm.

  - Phần 01 đến 03 bạn đã điền từ Build 3; dành thời gian cho phần 04 đến 07
  - Phần 04 ghi cỡ mẫu và gắn nhãn "provisional"
  - Phần 06 gọi tên chủ sở hữu có chủ ý, vì đó là người bạn sẽ pitch tiếp theo
  - Phần 07, điều gì sẽ khiến mình đổi ý, làm hồ sơ đáng tin

  > **Quyết định mà kết quả nào cũng không đảo ngược được thì không phải evidence-based.**

- 🎨 Visual hint: theo deck (slide 42).

---

### NUMBERED · Chuẩn bị sẵn câu trả lời cho những ý này
- Kicker: Chuẩn bị
- Title: Bốn câu chủ sở hữu hỏi
- On-slide: "Team mình chia như vậy mà." | Quyền sở hữu vẫn giữ nguyên. Chỉ vị trí hiển thị thay đổi. | "User sẽ tự search thôi." | Search cũng chạy trên chính các nhãn đó. Hãy xin log để xem. | "Không đụng được nav cũ." | Một giai đoạn, một điểm vào, test trước. | "Mới có năm người thôi." | Đồng ý trước đã. Pilot chỉ giúp tìm ra câu hỏi.
- Giờ: 3 phút (đề xuất)
- Ví dụ: bản nháp (câu trả lời cho "Team mình chia như vậy mà"). Cần ví dụ thật: một lần bạn bị phản đối thật khi đề xuất đổi cấu trúc, gồm ai nói gì, bạn trả lời ra sao và kết quả thế nào; đây là chỗ mentee học nhiều nhất
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Owner nói: "Team mình chia như vậy mà." Bạn sẽ trả lời gì?

  - Một câu trả lời tốt: "Đúng, và quyền sở hữu vẫn thuộc team anh. Chỉ vị trí hiển thị cho khách là thay đổi, vì khách không biết ai sở hữu gì." Sau đó đưa một con số từ tree test
  - 02 "User sẽ tự search": search chạy trên chính các nhãn đó; xin log, nhiều lượt tìm "where is my order" nghĩa là cấu trúc đã thất bại
  - 03 "Không đụng được nav cũ": một giai đoạn, một điểm vào, test trước
  - 04 "Mới có năm người": nói trước khi họ nói; pilot chỉ giúp tìm ra câu hỏi, không phải bằng chứng
  - Luyện câu trả lời, không học thuộc

  > **Công nhận điều đúng trước, rồi đổi vị trí hiển thị chứ không động vào quyền sở hữu.**

  > Chủ sở hữu của bạn sẽ có phản biện nào khác? Hãy thêm một ý của chính bạn để dùng ở vòng sau.

- 🎨 Visual hint: theo deck (slide 43).

---

### PRACTICE · Bảo vệ
- Num: 10
- Kicker: Bảo vệ
- Title: Pitch cho người mất nhiều nhất
- On-slide: Sản phẩm · ia-decision-record.md | Bốn vòng | Thứ tự các vòng | 01 | Hoàn thiện hồ sơ: phần 4 đến 7 | 2 phút | 02 | Pitch: hệ quả, bằng chứng, quyết định đề xuất | 2 phút | 03 | Phản biện: bốn ý phản đối, cộng thêm một ý của chính bạn | 3 phút | 04 | Coaching: chỗ bạn nói quá bằng chứng, chỗ bạn nhượng bộ | 3 phút
- Giờ: 10 phút (theo deck: 2 hoàn thiện hồ sơ, 2 pitch, 3 phản biện, 3 coaching)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Bảo vệ, mười phút, bốn vòng. Mình đóng vai chủ mục bị mất nhiều nhất trong danh sách owner của bạn.

  - Bốn vòng: hoàn thiện hồ sơ phần 04 đến 07, pitch, phản biện, coaching
  - Phản biện cuối lấy từ chính danh sách owner của bạn, không lấy từ slide
  - Coaching chỉ ra hai điều: chỗ bạn nói quá bằng chứng, và chỗ bạn nhượng bộ quá sớm để thắng tranh luận
  - Không cho điểm, chỉ ghi lại

  > **Pitch gồm hệ quả, bằng chứng và quyết định đề xuất.**

  > Phản biện gồm bốn ý phản đối, cộng thêm một ý của chính bạn.

- 🎨 Visual hint: theo deck (slide 44).

---

### STATEMENT · AI trong thực tế
- Kicker: AI trong thực tế
- Title: Dùng AI để thử thách ý tưởng, không phải để làm thay
- On-slide: "Đây là sitemap inherited, bộ thẻ và brief vấn đề của tôi. Hãy chỉ ra những thẻ dùng chung từ với nhãn của một mục, gợi ý ba task tree test bằng từ không có trong cây của tôi, và liệt kê các state còn thiếu trong flow của tôi." | Lưu ý | Kết quả card sort do AI sinh ra không phải nghiên cứu. Đưa nó ra như thật là bịa bằng chứng. | Thử | Nhờ AI đóng vai chủ mục và nêu ba phản biện mạnh nhất dựa trên các file của bạn.
- Giờ: [to confirm]
- Ví dụ: có (prompt mẫu trên slide: dán sitemap, bộ thẻ và brief, hỏi ba việc)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Dán sitemap inherited, bộ thẻ và brief vấn đề vào AI chat tool, rồi nhờ nó chỉ ra những thẻ dùng chung từ với nhãn của một mục, gợi ý ba task tree test bằng từ không có trong cây của bạn, và liệt kê các state còn thiếu trong flow.

  - AI đã có sẵn thư mục dự án, không cần giải thích lại
  - Dùng tốt: gom cụm kết quả thật, gợi ý nhãn thay thế để test, đóng vai chủ mục phản biện
  - Thử ngay: nhờ AI đóng vai chủ mục và nêu ba phản biện mạnh nhất dựa trên các file của bạn
  - AI không biết bước nào là ràng buộc kỹ thuật thật; hỏi engineering trước khi tô đỏ

  > **Kết quả card sort do AI sinh ra trông thật nhưng không phải nghiên cứu. Đưa ra như thật là bịa bằng chứng.**

  > Dùng AI để thử sức chịu đựng của ý tưởng, không phải để làm thay.

- 🎨 Visual hint: theo deck (slide 45).

---

### NUMBERED · Trước buổi sau
- Kicker: Bài về nhà
- Title: Trước buổi sau
- On-slide: 01 | Chạy card sort: nhắm khoảng 15 người, dưới 5 người thì ghi là provisional | 02 | Tree test cả hai cây với ba task của bạn | 03 | Hoàn thiện flow: diamond có nhãn, các bước đỏ có ghi chú | 04 | Điền hồ sơ bằng số liệu thật | 05 | Pitch cho owner. Ghi lại họ nói gì và bạn đã nhượng bộ điều gì | Cách kiểm tra: owner có tự giải thích được thay đổi mà không nhắc tới card sorting không?
- Giờ: [to confirm]
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Bài tập mất ba đến bốn giờ, trong một đến hai tuần. Cách kiểm tra thành công: owner có tự giải thích được thay đổi mà không nhắc tới card sorting không?

  - Thứ tự làm: chạy card sort khoảng 15 người, dưới 5 người thì ghi provisional; tree test cả hai cây với ba task; hoàn thiện flow với diamond có nhãn và bước đỏ có ghi chú
  - Điền hồ sơ bằng số liệu thật, rồi pitch cho owner; ghi lại họ nói gì và bạn đã nhượng bộ điều gì
  - Nếu owner nói về phương pháp, bạn đang tranh luận nghiên cứu, không phải quyết định
  - Mang cả hai sitemap và flow sang buổi Design; các bước đỏ là vấn đề thiết kế đầu tiên

  > **Owner giải thích được thay đổi mà không nhắc tới card sorting.**

- 🎨 Visual hint: theo deck (slide 46).

---

### END · Tiếp theo · Design
- Kicker: Tiếp theo · Design
- Title: Cảm ơn bạn!
- On-slide: Winnie Nguyen · nguyenphuctuongvan@gmail.com
- Giờ: [to confirm]
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Buổi Design làm việc trong cây đã test hôm nay, nên bài tập là điều kiện đầu vào.

  - Chốt ngày chia sẻ kết quả nghiên cứu
  - Kết bằng một câu hỏi mở và mời mentee gửi câu hỏi qua chat

  > Bạn còn câu hỏi nào không? Cảm ơn bạn.

- 🎨 Visual hint: theo deck (slide 47).
