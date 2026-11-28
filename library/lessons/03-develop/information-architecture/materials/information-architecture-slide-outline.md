---
title: "Information Architecture"
lesson_file: "information-architecture-lesson.md"
level: ""
slide_count: 44
duration: "120–135 min"      # [to confirm] khớp với lesson cũ; deck không ghi tổng giờ
status: matches-built-deck
built_deck: "https://claude.ai/artifact/2GcoGVH1bSg29CUWZ1NcY6"
last_synced: 2026-11-28
---

> **Source of truth:** `information-architecture-lesson.md`
> Outline này được dựng lại từ deck Slides mới (44 slide, dựng theo skill slide-deck, deck wins theo Deck edit rule trong `CLAUDE.md`). Bản cũ (47 slide, từ deck Claude Design) nằm ở `_archive/information-architecture-slide-outline-pre-deck-sync-2026-11-28.md`.
> Speaker notes chép nguyên văn từ deck, mỗi đoạn là một dòng `>`; chưa tách thành bullet nên `notes-audit.py` sẽ báo thiếu bullet. Ví dụ `bản nháp` vẫn chờ Winnie xác nhận.

---

## Session metadata

| Field | Value |
|---|---|
| Program | private-training / ux-class `[to confirm]` |
| Track / session | Deck ghi "Buổi 5"; lesson cũ ghi session 04 và 05 (ui-ux-fundamentals) và (junior-to-mid-level) `[to confirm]` |
| Stage | Develop |
| Prior session | Synthesis & Problem Definition |
| Next session | Design |
| Running example | Food delivery (sitemap, card sort, user flow, process map); Travel Buddy ở phần AI |

---

## Slide structure — 44 slides

- Arc: **Mở bài** (slide 1 đến 3) → **Phần 1** Inherited vs Evidence-Based (4 đến 6) → **Phần 2** Sitemap (7 đến 10) → **Phần 3** Card Sorting (11 đến 16) → **Phần 4** User Flows (17 đến 24) → **Phần 5** Process Map (25 đến 32) → **Phần 6** AI cho flow (33 đến 41) → **Activity và bài tập** (42, 43) → **Kết** (44).
- Mọi activity dồn xuống cuối deck (Winnie chốt 2026-11-28). Deck có một Activity 30 phút (slide 42) và một bài tập về nhà (slide 43), cả hai chỉ còn user flow hoặc process map. Các Build, Hoạt động và Bảo vệ của outline cũ không còn trong deck.
- Deck mới không còn Tree Testing, Defend Your IA và `ia-decision-record.md` ở dạng slide; cover vẫn nhắc `ia-decision-record.md` ở notes `[to confirm]`.
- Phần 6 có hai slide thêm từ bài Explore Ideas: `ai-order` (bạn nghĩ trước, AI đến sau) và `ai-views` (một nguồn, nhiều view).
- Deck mới không ghi thời lượng từng Phần. Số phút của outline cũ đã bỏ.
- Title slide có thể dài hơn 6 từ ở slide tiêu đề câu (ví dụ `cardsort-results`); `/notes-audit` có thể báo.

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
- Right panel photo: ảnh bàn tay vẽ sơ đồ luồng trên giấy (Winnie cung cấp 2026-11-28; nguồn và giấy phép `[to confirm]`)
- Ví dụ: Không cần (slide mở đầu).
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Buổi trước chúng ta đã chốt xong vấn đề. Hôm nay mở sang phần giải pháp, ở cấp độ cấu trúc.

  > Hôm nay không vẽ màn hình. Mọi thứ là cây, bộ thẻ, luồng hoặc hồ sơ quyết định. Đầu ra duy nhất là ia-decision-record.md, kèm một lần pitch cho người sở hữu mục bạn muốn dời.

  > Cuối buổi, bạn bảo vệ phương án của mình trước chính người sở hữu mục đó.

  > Câu hỏi cho bạn: Bạn đã bao giờ thử vẽ lại menu của sản phẩm mình đang làm chưa?

- 🎨 Visual hint: theo deck (slide 1, id `cover`).

---

### STATEMENT · Brief của bạn đã nói vấn đề là gì. Nhưng chưa nói mọi thứ đang nằm ở đâu.
- Kicker: Buổi trước mình dừng ở đâu
- Title: Brief của bạn đã nói vấn đề là gì.\n*Nhưng chưa nói mọi thứ đang nằm ở đâu.*
- On-slide: Kết luận chẩn đoán, giờ đặt lại thành một câu hỏi về cấu trúc.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Chúng ta đọc to bản chẩn đoán của buổi trước, giữ nguyên chữ. Câu chẩn đoán nằm trong brief của bạn, nên bạn tự đọc, không ai đọc thay.

  > Slide này chuyển chúng ta từ “vấn đề là gì” sang “vấn đề nằm ở đâu trong cấu trúc”. Câu trả lời thường là ở ba nơi, của ba team, và đó là chất liệu của cả buổi hôm nay.

  > Câu hỏi cho bạn: Vấn đề này đang nằm ở đâu trong sản phẩm của bạn?

- 🎨 Visual hint: theo deck (slide 2, id `statement-last`).

---

### NUMBERED · Mục tiêu buổi học
- Kicker: Tổng quan buổi
- Title: Mục tiêu\n*buổi học*
- On-slide: Bạn đi từ một câu hỏi đến một quyết định bạn bảo vệ được. | 01 | Inherited vs evidence-based: nhận ra cấu trúc thừa hưởng | 02 | Sitemap: vẽ cây hiện tại từ sản phẩm thật | 03 | Card sorting: xem khách hàng tự nhóm thế nào | 04 | User flow: xem cấu trúc này bắt user trả giá những gì | 05 | Process map: xem ai làm gì phía sau màn hình | 06 | AI cho flow
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Hôm nay có sáu phần, đi theo thứ tự từ 01 đến 06. Thứ tự này có lý do: chúng ta vẽ cây hiện tại trước khi sort, vì thẻ card sort lấy từ sitemap.

  > Phần 1 giúp bạn nhận ra cấu trúc thừa hưởng. Phần 2 và 3 là sitemap và card sorting, đi từ cây đang có sang cách khách hàng tự nhóm. Phần 4 và 5 là user flow và process map, cho thấy cấu trúc bắt user trả giá gì và ai làm gì phía sau màn hình. Phần 6 là cách dùng AI cho flow.

  > Cuối buổi, bạn đi từ một câu hỏi đến một quyết định mà bạn bảo vệ được.

- 🎨 Visual hint: theo deck (slide 3, id `agenda`).

---

### SECTION DIVIDER · Inherited vs Evidence-Based
- Num: 01
- Kicker: Inherited vs Evidence-Based
- Title: Inherited vs Evidence-Based
- Sub: Hầu hết designer nhận IA có sẵn rồi dùng luôn, không hỏi lại.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Phần đầu chỉ có một mục tiêu: bạn tự nhận ra dấu hiệu sơ đồ tổ chức trong chính sản phẩm của mình. Đây là phần ngắn nhất, và chúng ta không đi sâu vào định nghĩa.

  > Hầu hết designer thừa hưởng IA có sẵn và không bao giờ đặt câu hỏi cho nó. Slide kế tiếp sẽ cho bạn câu hỏi để tự trả lời.

  > Câu hỏi cho bạn: Mục nào trong menu của bạn chỉ giải thích được bằng tên team?

- 🎨 Visual hint: theo deck (slide 4, id `divider-01`).

---

### STATEMENT · IA quyết định cái gì nằm ở đâu
- Kicker: Định nghĩa
- Title: IA quyết định\n*cái gì nằm ở đâu*
- On-slide: Tên gọi là gì, và đi tới đó bằng cách nào.
- Ví dụ: bản nháp (app ngân hàng xếp theo dòng sản phẩm: Cards, Loans, Savings)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Một app ngân hàng có Cards, Loans, Savings vì mỗi mục do một team giữ. Khách chỉ hỏi: tiền của tôi đang ở đâu?

  > IA là cách tổ chức, đặt tên và sắp xếp nội dung để người dùng tìm được thứ họ cần. Nó quyết định ba thứ: cái gì nằm ở đâu, tên gọi là gì, và đi tới đó bằng cách nào. Với người đã senior, chúng ta không định nghĩa dài dòng.

  > Vậy ai làm IA, và ai quyết định? Người làm là UX hoặc Product designer, hoặc IA specialist, cùng PM và content. Họ vẽ sitemap, chạy card sort và tree test rồi đề xuất cấu trúc. Người quyết định thường là PO, owner của từng mục, hoặc hệ thống cũ từ nhiều năm trước. Designer đề xuất, owner mới là người quyết định. Vì vậy cuối buổi bạn phải pitch cho owner, không chỉ vẽ cho đẹp.

  > Câu hỏi cho bạn: Sản phẩm của bạn có mục nào đặt tên theo team không?

- 🎨 Visual hint: theo deck (slide 5, id `definition`).

---

### COMPARE · Hai cách làm IA
- Kicker: So sánh
- Title: Hai cách làm *IA*
- On-slide: Inherited IA | Nguồn | PO, stakeholder, hệ thống cũ | Logic | Theo team, theo quyền sở hữu tính năng, theo hệ thống | Rủi ro | “Nghe hợp lý với bên mình” | Evidence-Based IA | Nguồn | Card sort, tree test, dữ liệu search và support | Logic | Theo mental model và task của user | Rủi ro | Cần thời gian và kỷ luật phương pháp | Cách nhận ra: nếu một mục chỉ có lý khi bạn nói ra ai sở hữu nó, thì đó là cấu trúc inherited.
- Ví dụ: bản nháp (Support, Orders, Account so với Đơn của tôi, Sự cố với đơn, Thanh toán)
- Câu hỏi hay gặp:
  - Inherited có phải luôn sai không? Không; chỉ là chưa được kiểm chứng.
  - Có phải lúc nào cũng làm evidence-based đủ bộ không? Không; nó tốn thời gian nên không phải lúc nào cũng làm đủ.
- Speaker notes:

  > Đây là hai cách làm IA mà chúng ta hay gặp. Bên trái là inherited: Support, Orders, Account, tức là ba team. Bên phải là evidence-based: Đơn của tôi, Sự cố với đơn, Thanh toán, tức là ba việc khách muốn làm. Nội dung giống nhau, chỉ khác cách chia.

  > Với inherited, nguồn là PO, stakeholder và hệ thống cũ, logic theo team, và rủi ro là “nghe hợp lý với bên mình”. Inherited không phải lúc nào cũng sai, nó chỉ là chưa được kiểm chứng.

  > Với evidence-based, nguồn là card sort, tree test, dữ liệu search và support, còn logic theo mental model và task của user. Đây không phải ý kiến của designer, nên mới có dòng Nguồn. Cái giá là cần thời gian và kỷ luật phương pháp, vì vậy không phải lúc nào chúng ta cũng làm đủ bộ.

  > Cách nhận ra: nếu một mục chỉ có lý khi bạn nói ra ai sở hữu nó, thì đó là cấu trúc inherited.

  > Câu hỏi cho bạn: Sản phẩm của bạn đang ở cột nào, và mục cấp 1 nào qua được bài kiểm tra này?

- 🎨 Visual hint: theo deck (slide 6, id `compare-ia`).

---

### SECTION DIVIDER · Sitemap
- Num: 02
- Kicker: Sitemap
- Title: Sitemap
- Sub: Vẽ cây hiện tại của sản phẩm, trước khi có ý kiến về cách sửa.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Phần này chỉ có một việc: vẽ cây hiện tại của sản phẩm, từ sản phẩm thật. Phần 1 vừa cho chúng ta thấy cấu trúc nào là thừa hưởng, nên bây giờ cần một bản đồ đầy đủ để nhìn vào.

  > Chúng ta chưa có ý kiến về cách sửa. Sitemap là chất liệu cho card sort ở phần sau.

  > Vẽ từ sản phẩm thật, không vẽ từ trí nhớ.

- 🎨 Visual hint: theo deck (slide 7, id `divider-02`).

---

### NUMBERED · What is X · Sitemap là gì?
- Kicker: Định nghĩa
- Title: Sitemap\n*là gì?*
- On-slide:
  - What: Mọi màn hình và mục user đang chạm vào hôm nay, xếp lồng nhau từ cha đến con, đúng như sản phẩm thật.
  - Why: Chưa kiểm kê nội dung thì không viết được bộ thẻ. Sitemap cũng phơi ra dấu hiệu “sơ đồ tổ chức” ngay trên bảng, trước khi có bằng chứng từ user.
  - When: Làm trước card sorting, khi bạn chưa có ý kiến về cách sửa. Các thẻ sau này lấy thẳng từ danh sách này.
- Ví dụ: có (Food delivery, slide kế tiếp)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Sitemap là mọi màn hình và mục user đang chạm vào hôm nay, lồng nhau từ cha đến con, đúng như sản phẩm thật.

  > Chúng ta cần nó vì chưa kiểm kê nội dung thì không viết được bộ thẻ cho card sorting. Sitemap cũng phơi ra dấu hiệu sơ đồ tổ chức ngay trên bảng, trước khi có bằng chứng từ user để phản biện.

  > Làm sitemap trước card sorting, khi bạn chưa có ý kiến về cách sửa. Nếu đã có ý kiến, bạn sẽ vẽ sitemap theo hướng đã chọn sẵn.

  > Đây là sitemap của sản phẩm đang chạy, không phải bản thiết kế mong muốn, nên bạn vẽ từ sản phẩm thật chứ không vẽ từ trí nhớ. Slide sau cho chúng ta xem một sitemap như vậy.

- 🎨 Visual hint: theo deck (slide 8, id `sitemap-what`).

---

### DIAGRAM · Sitemap food delivery
- Kicker: Ví dụ
- Title: Sitemap food delivery
- On-slide: Food Delivery App | Home | Search | Offers | Growth | Orders | Operations | Account | Customer Service | Current | Order detail | Track | Help Centre | Order issues | Hai chỗ khách có thể tìm đơn trễ, do hai team giữ
- Ví dụ: có (Food delivery trên slide)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Khách đang lo vì đơn trễ. Nếu bạn là khách, bạn sẽ bấm vào đâu đầu tiên?

  > Hai mục tô tím là hai chỗ khách có thể đi. Tracking nằm ở Orders, do team Operations giữ. Tin nhắn “đơn trễ” nằm ở Help, do team Customer Service giữ. Còn hoàn tiền thì nằm ở Account. Một nỗi lo của khách bị chia cho ba team.

  > Đây là khảo cổ, không phải phán xét, nên chúng ta không đổ lỗi cho team nào.

- 🎨 Visual hint: SCHEMATIC · theo deck (slide 9, id `diagram-sitemap`).

---

### IMAGE · Travel Buddy: bảy nhóm
- Kicker: Ví dụ · Sitemap
- Title: Travel Buddy: bảy nhóm
- On-slide: Do AI dựng từ card sort. Hai nhóm đầu là lối vào và hub, năm nhóm sau là content pillar.
- Ví dụ: có (Travel Buddy, bảy nhóm dưới một app)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là sitemap do AI dựng cho Travel Buddy, từ kết quả card sort.

  > Có bảy nhóm dưới một app: Onboarding, Dashboard, Discover, Plan / Trip, Connect, Journal / Memories, Profile & Settings. Hai nhóm đầu là lối vào và điểm quay về, năm nhóm sau là content pillar. Mỗi nhóm liệt kê các màn hình bên trong.

  > Đường cam là giả thuyết rủi ro nhất: user có thể gộp Discover và Plan / Trip, trùng với giả thuyết ở card sort.

  > Câu hỏi cho bạn: Nhóm nào trong sitemap của bạn là giả thuyết rủi ro nhất?

- 🎨 Visual hint: REAL · theo deck (slide 10, id `example-sitemap`).

---

### SECTION DIVIDER · Card Sorting
- Num: 03
- Kicker: Card Sorting
- Title: Card Sorting
- Sub: Khách hàng sẽ nhóm và đặt tên cho những gì bạn vừa vẽ ra sao.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Phần này dùng đúng các thẻ từ sitemap bạn vừa vẽ, nên bạn giữ file đó mở.

  > Card sort không cho chúng ta biết thiết kế thế nào. Nó cho biết khách nghĩ thế nào.

  > Câu hỏi cho bạn: Khách hàng sẽ nhóm và đặt tên cho những gì bạn vừa vẽ ra sao?

- 🎨 Visual hint: theo deck (slide 11, id `divider-03`).

---

### NUMBERED · What is X · Card Sorting là gì?
- Kicker: Định nghĩa
- Title: Card Sorting\n*là gì?*
- On-slide:
  - What: User sắp xếp sticky note thành nhóm, rồi tự đặt tên cho nhóm.
  - Why: Phơi bày mental model của user, thay cho cấu trúc không còn phù hợp.
  - When: Cấu trúc mới hoặc bị nghi ngờ, phân loại khó hiểu, hoặc trước khi chốt sitemap.
- Ví dụ: bản nháp (app giao đồ ăn: khách tìm “hoàn tiền” trong Orders, team đặt dưới Help)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Một app giao đồ ăn có ba nhóm: Orders, Help, Account. Khách tìm “hoàn tiền” ở đâu?

  > Card sorting là người dùng sắp xếp các thẻ nội dung thành nhóm theo cách họ nghĩ, rồi đặt tên cho nhóm. Mục tiêu là làm lộ ra mental model của họ, thay vì cấu trúc theo team hay hệ thống cũ. Mental model là hình dung sẵn trong đầu user về việc mọi thứ nên nằm ở đâu và gọi là gì. Ví dụ, khách tìm “hoàn tiền” trong Orders, trong khi team đặt nó dưới Help. Người dùng không đọc sitemap của chúng ta, họ dùng hình dung của chính họ.

  > Chúng ta dùng card sorting khi cấu trúc mới hoặc đang bị nghi ngờ, khi nhãn khó hiểu, hoặc trước khi quyết định sitemap.

  > Câu hỏi cho bạn: Bạn đang cần biết nhóm, hay cần biết nhãn?

- 🎨 Visual hint: theo deck (slide 12, id `cardsort-what`).

---

### COMPARE · Ba định dạng card sort
- Kicker: So sánh
- Title: Ba định dạng *card sort*
- On-slide: Open | Họ tự tạo nhóm và đặt tên | Dùng khi bạn không tin cấu trúc hiện tại | Lộ ra mental model, bằng chính lời của họ | Closed | Họ sort vào nhóm của bạn | Dùng để test nhãn | Cho biết tên gọi có dễ hiểu không | Hybrid | Nhóm của bạn, cộng thêm chỗ để họ tự thêm | Dùng để tìm chỗ còn thiếu | Chọn định dạng theo câu hỏi bạn cần trả lời.
- Ví dụ: bản nháp (sitemap ba nhóm Orders, Help, Account)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Giả sử một app giao đồ ăn có sitemap ba nhóm: Orders, Help, Account. Câu hỏi của team là gì? Khách nhóm thế nào, hay tên gọi của mình có dễ hiểu không?

  > Open sort: họ tự tạo nhóm và đặt tên. Chúng ta dùng khi không tin cấu trúc hiện có, vì nó lộ ra mental model bằng chính lời của họ.

  > Closed sort: họ sort vào nhóm của chúng ta. Đây là bài test nhãn, không phải test cấu trúc.

  > Hybrid: nhóm của chúng ta cộng thêm chỗ để họ tự thêm, dùng để tìm chỗ còn thiếu. Cách này thực tế nhất khi phần lớn cây vẫn ổn.

  > Chọn định dạng theo câu hỏi bạn cần trả lời. Phần đông senior mặc định chọn open, và với dự án nhỏ, bạn bắt đầu bằng open sort 5 người rồi quyết định.

  > Câu hỏi cho bạn: Bạn đang cần biết nhóm, hay cần biết nhãn?

- 🎨 Visual hint: theo deck (slide 13, id `cardsort-formats`).

---

### DIAGRAM · Đọc kết quả card sort
- Kicker: Cách đọc
- Title: Đọc kết quả *card sort*
- On-slide: Agreement cho bạn biết các nhóm. Divergence cho bạn biết vấn đề nằm ở đâu. | Thẻ “Đồ ăn của tôi bị trễ”: 15 người sort (số minh họa) | Nó đang ở đâu | 9 người · agreement | Hỗ trợ | 4 người | Đơn hàng | 2 người | Sáu người còn lại là divergence: thẻ này cần tìm được từ nhiều chỗ. | 5 người = pilot · khoảng 15 người = open sort đáng tin
- Ví dụ: bản nháp (15 người sort thẻ “đồ ăn của tôi bị trễ”, số minh họa)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Mười lăm người sort thẻ “đồ ăn của tôi bị trễ”: chín người xếp vào “Nó đang ở đâu”, bốn vào “Hỗ trợ”, hai vào “Đơn hàng”. Đây là số minh họa.

  > Chín người đồng ý là một nhóm rõ, kèm tên nhóm họ đặt. Đó là agreement. Sáu người còn lại cho biết thẻ này cần tìm được từ ba chỗ. Divergence cũng là dữ liệu: thẻ bị rải ra nhiều nhóm nghĩa là khách muốn tìm nó từ nhiều chỗ, không phải khách sort sai.

  > Agreement cho chúng ta biết các nhóm, còn divergence cho biết vấn đề nằm ở đâu.

  > Mỗi lần báo kết quả, bạn nói cỡ mẫu ngay câu đầu: 5 người là pilot, khoảng 15 người mới đáng tin với open sort.

- 🎨 Visual hint: SCHEMATIC · theo deck (slide 14, id `cardsort-results`).

---

### IMAGE · Travel Buddy
- Kicker: Ví dụ
- Title: Travel Buddy
- On-slide: Do AI dựng từ Solution Pool. Mỗi thẻ mang ID của solution. Đường cam là giả thuyết cần test.
- Ví dụ: có (Travel Buddy, năm nhóm từ Solution Pool)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là một card sort do AI dựng cho Travel Buddy, từ Solution Pool.

  > Có năm nhóm: Discover (6 thẻ), Plan / Trip (7), Connect (5), Journal / Memories (5), Settings / Account (3). Mỗi thẻ là một solution và mang ID từ Solution Pool, như D1, P3, C2, nên chúng ta lần ngược lại được nguồn.

  > Đường cam là giả thuyết cần test: user có gộp Discover và Plan / Trip thành một nhóm không? Đây là bản nháp của team, chưa phải kết quả của user. Open sort với user mới cho biết họ nhóm thế nào.

  > Câu hỏi cho bạn: Bạn sẽ test giả thuyết nào trước?

- 🎨 Visual hint: REAL · theo deck (slide 15, id `example-cardsort`).

---

### IMAGE · ReferPlus 2019
- Kicker: Ví dụ
- Title: ReferPlus 2019
- On-slide: Hai nhóm user là recruiter và headhunter, dùng chung một sản phẩm | Cách làm: gặp trực tiếp, dùng whiteboard, với team nội bộ | Đầu ra: cấu trúc navigation và sitemap
- Ví dụ: có (ReferPlus 2019, card sort trên whiteboard với team nội bộ)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là một bài card sort mình làm năm 2019 cho ReferPlus, một sản phẩm có hai nhóm user là recruiter và headhunter dùng chung.

  > Chúng mình làm trực tiếp trên whiteboard, với team nội bộ, và đầu ra là cấu trúc navigation và sitemap.

  > Đây là phương pháp tốt, nhưng người tham gia là nội bộ nên bài sort chỉ phản ánh giả định của team, chưa phải bằng chứng người dùng.

  > Câu hỏi cho bạn: Cần thêm gì để gọi nó là evidence-based? Câu trả lời mong đợi là cùng bài sort với recruiter và headhunter thật, rồi tree test.

- 🎨 Visual hint: REAL · theo deck (slide 16, id `referplus`).

---

### SECTION DIVIDER · User Flows
- Num: 04
- Kicker: User Flows
- Title: User Flows
- Sub: Màn hình đẹp nằm trong flow sai thì vẫn là thiết kế hỏng.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Ở phần này, user flow chỉ có một việc: cho thấy cấu trúc hiện tại tốn gì ở một task cốt lõi, như “xem đơn đang giao”. Chúng ta giữ phần này gọn, vì bạn đã học flow ở buổi khác. Mục tiêu duy nhất là dùng flow để đo cái giá của cấu trúc.

  > Màn hình đẹp nằm trong flow sai thì vẫn là thiết kế hỏng.

- 🎨 Visual hint: theo deck (slide 17, id `divider-04`).

---

### NUMBERED · What is X · User flow là gì?
- Kicker: Định nghĩa
- Title: User flow\n*là gì?*
- On-slide:
  - What: Các bước một user đi qua để xong một task, từ điểm vào đến kết quả. Nó không phải wireframe.
  - Why: Xác định đường đi của task trước khi vẽ màn hình, và tìm friction cùng state còn thiếu khi sửa còn rẻ.
  - When: Trước khi wireframe, khi rà soát sản phẩm cũ, khi tìm chỗ user bỏ đi hoặc bị lạc, và khi bàn giao cho engineering.
- Ví dụ: bản nháp (đặt và xác nhận một slot)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Một user flow cho task “Đặt và xác nhận một slot” không vẽ mười màn hình. Nó chỉ vẽ sáu bước và hai điểm quyết định.

  > Chúng ta nói sớm: user flow không phải wireframe, vì nhiều người vẽ hộp màn hình rồi gọi là flow. Nó là các bước một user đi qua để xong một task, từ điểm vào đến kết quả. Nhấn vào “một người, một task”.

  > Mục tiêu là xác định đường đi của task trước khi vẽ màn hình, và tìm ma sát cùng state còn thiếu khi sửa vẫn còn rẻ.

  > Chúng ta dùng flow trước wireframe, khi rà soát sản phẩm cũ, khi tìm chỗ user rơi rụng, và khi bàn giao cho engineering.

  > Câu hỏi cho bạn: Flow trong dự án của bạn có đúng là một người, một task không?

- 🎨 Visual hint: theo deck (slide 18, id `flow-what`).

---

### COMPARE · Phạm vi của user flow
- Kicker: Phạm vi
- Title: Phạm vi của *user flow*
- On-slide: Trong phạm vi | Một user, một task, một điểm vào | Màn hình, hành động, quyết định | Những gì user nhìn thấy | Ngoài phạm vi | Các actor khác (admin, support, payment provider) | Việc hệ thống làm phía sau | Bàn giao nội bộ, thuộc về Process Map | Khi không có user flow | Thiết kế màn hình mà không biết trước và sau nó là gì | State lỗi và edge case chỉ lộ ra khi dev | Stakeholder cãi chi tiết màn hình khi chưa thống nhất cấu trúc task
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Phần lớn vấn đề thiết kế nằm ở flow, không nằm ở màn hình.

  > Trong phạm vi của user flow là một user, một task, một điểm vào; màn hình, hành động, quyết định; và những gì user nhìn thấy. Ngoài phạm vi là các actor khác, việc hệ thống làm phía sau, và bàn giao nội bộ. Giữ phạm vi này giúp flow dễ đọc.

  > Còn khi bỏ qua flow, chúng ta trả ba cái giá: thiết kế màn hình mà không biết trước và sau nó là gì; state lỗi và edge case chỉ lộ ra khi dev; và stakeholder cãi chi tiết màn hình khi chưa thống nhất cấu trúc của task.

- 🎨 Visual hint: theo deck (slide 19, id `flow-scope`).

---

### PROCESS · Cách vẽ một user flow
- Kicker: Phương pháp
- Title: Cách vẽ một *user flow*
- On-slide: 01 | Đặt khung | Đặt tên task cụ thể, không phải “checkout” | Vẽ pill Start và End trước | 02 | Vẽ flow | Happy path trước | Thêm nhánh lỗi và edge case | Ghi chú chỗ có friction | 03 | Kiểm tra | Mỗi diamond có hai mũi tên ra, đều có nhãn | Không để hình nào bị bỏ lẻ
- Ví dụ: bản nháp (đặt và xác nhận một slot, user đã dùng app trước đó)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Chúng ta vẽ theo ba nhóm việc, với sáu bước. Không phải “checkout”, mà là “đặt và xác nhận một slot, user đã dùng app trước đó”. Đặt tên task cụ thể để flow không quá rộng, rồi vẽ Start và End trước.

  > Tiếp theo là vẽ flow: happy path trước, rồi thêm nhánh lỗi và edge case. Bước nhánh lỗi là nơi lộ state còn thiếu, nên đi chậm ở đây. Sau đó ghi chú chỗ có ma sát, và ghi rõ nó tốn gì.

  > Cuối cùng là kiểm tra: mỗi diamond có hai mũi tên ra, đều có nhãn, và không có hình nào bị bỏ lẻ. Mỗi nhánh phải có đích, không để mũi tên treo.

- 🎨 Visual hint: theo deck (slide 20, id `flow-method`).

---

### NUMBERED · Năm hình của user flow
- Kicker: Cấu tạo
- Title: Năm hình\n*của user flow*
- On-slide: Dùng hình nhất quán thì cả team đọc được flow mà không cần giải thích. | Pill | Điểm bắt đầu và kết thúc, ví dụ “User mở app” | Rectangle | Một màn hình hoặc hành động của user, ví dụ “Xem danh sách slot” | Diamond | Điểm quyết định, ví dụ “Slot còn trống không?” | Arrow | Hướng đi của flow, gắn nhãn cho nhánh như Yes / No | Note | Ngữ cảnh không nhét vừa một hình, ví dụ “Friction: phải bấm 3 lần mới tới đây”
- Ví dụ: có (ví dụ trên từng hình: “User mở app”, “Slot còn trống không?”)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Năm hình mang toàn bộ ý nghĩa, và chúng ta đi qua trong khoảng một phút.

  > Pill là điểm bắt đầu và kết thúc. Rectangle là một màn hình hoặc hành động của user. Diamond là điểm quyết định, và có đúng hai mũi tên ra, đều có nhãn như Yes và No. Arrow là hướng đi của flow. Note là ngữ cảnh không nhét vừa một hình, ví dụ “Friction: phải bấm 3 lần mới tới đây”.

  > Dùng hình nhất quán thì cả team đọc được flow mà không cần giải thích. Nếu cần hình thứ sáu, đó thường là một bước của hệ thống, tức là chuyện của process map.

- 🎨 Visual hint: theo deck (slide 21, id `flow-shapes`).

---

### DIAGRAM · Đặt và xác nhận một slot
- Kicker: Ví dụ
- Title: Đặt và xác nhận một slot
- On-slide: Start | Chọn slot | Slot còn trống? | Thanh toán | Xem lại đặt chỗ | Thanh toán OK? | Đã xác nhận | End | YES | NO | YES | NO | Màn hình hiện “pending”, không phải “confirmed”. | Flow chỉ cho thấy những gì user thấy, nên không giải thích được vì sao hiện “pending”.
- Ví dụ: có (đặt và xác nhận một slot; màn hình hiện “pending”)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Ở bước cuối, màn hình xác nhận hiện “pending”, không phải “confirmed”. Tại sao lại là pending?

  > Chúng ta đi từ trái sang phải, rồi xuống và quay ngược ở hàng hai. Dừng ở diamond “Slot còn trống?” và nhánh lỗi thanh toán.

  > Hãy để bạn đoán trước khi sang phần Process Map. Gợi ý đáp án: đơn vượt hạn mức tự duyệt và đang chờ Ops team. Màn hình không có lỗi, quy trình phía sau mới là nguyên nhân.

  > Flow chỉ cho thấy những gì user thấy, nên không giải thích được vì sao hiện “pending”. Câu trả lời nằm ở phần Process Map.

- 🎨 Visual hint: SCHEMATIC · theo deck (slide 22, id `flow-example`).

---

### NUMBERED · Ba điều flow cho bạn thấy
- Kicker: Đọc flow
- Title: Ba điều flow\n*cho bạn thấy*
- On-slide: Task cốt lõi mà dài hơn 7 bước thì nhiều khả năng lỗi nằm ở IA, không phải ở thiết kế màn hình. | 01 | Điểm quyết định bắt user làm việc mà hệ thống có thể tự xử lý | 02 | Flow dài hơn mức cần thiết vì nội dung nằm sai chỗ trong IA | 03 | Thiếu state: empty, error, loading, success
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Task cốt lõi của bạn có bao nhiêu bước? Nếu nó dài hơn bảy bước thì nhiều khả năng lỗi nằm ở IA, không phải ở thiết kế màn hình.

  > Có ba điều cần tìm trong một flow. Một là quyết định mà user phải làm thay cho việc hệ thống có thể tự xử lý. Hai là flow dài hơn mức cần thiết vì nội dung nằm sai chỗ trong IA. Ba là thiếu state: empty, error, loading, success.

  > Câu hỏi cho bạn: Task cốt lõi của bạn có bao nhiêu bước, và bước nào thuộc một trong ba nhóm này?

- 🎨 Visual hint: theo deck (slide 23, id `flow-good`).

---

### COMPARE · Đánh giá từng bước bằng JTBD
- Kicker: JTBD → Flow
- Title: Đánh giá từng bước *bằng JTBD*
- On-slide: Với mỗi bước, hãy hỏi: bước này giúp user tiến gần job của họ, hay chỉ là friction do hệ thống tự tạo ra? | User cần xác nhận nhanh trước khi mất slot | Không đặt màn hình upsell trên đường đi chính | User lo lắng về những hành động không thể hoàn tác | Thêm bước review trước khi xác nhận cuối cùng | User muốn trông chuyên nghiệp khi chia sẻ sản phẩm của mình | Đặt “share” ngay lúc hoàn thành task, đừng giấu trong settings
- Ví dụ: bản nháp (job: biết đơn có tới kịp trước 7 giờ không)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Chúng ta dùng JTBD map từ buổi trước. Với mỗi bước, hãy hỏi: bước này giúp user tiến tới job của họ, hay chỉ là ma sát do hệ thống tự tạo?

  > Ví dụ job “Tôi muốn biết đơn có tới kịp trước 7 giờ không.” Hệ quả cho flow là hiển thị giờ dự kiến ở màn hình đầu tiên, không cần bấm vào từng đơn.

  > Trên slide có ba cặp. User cần xác nhận nhanh thì không đặt upsell ở đường chính. User lo việc không thể hoàn tác thì thêm bước review. User muốn trông chuyên nghiệp khi chia sẻ thì đưa “share” ra lúc hoàn thành. Mỗi cặp nhu cầu của user và hệ quả cho flow là một quyết định thiết kế.

  > Câu hỏi cho bạn: Job nào trong JTBD map của bạn, và hệ quả cho flow của nó là gì?

- 🎨 Visual hint: theo deck (slide 24, id `flow-jtbd`).

---

### SECTION DIVIDER · Process Map
- Num: 05
- Kicker: Process Map
- Title: Process Map
- Sub: Lùi ra xa để thấy ai làm gì phía sau màn hình
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Nếu cùng một task, ai khác ngoài user đang làm việc? Bạn thử kể ba đến bốn actor trước khi chúng ta sang slide tiếp theo.

  > Process map là cùng một task với user flow, nhưng thu nhỏ lại để nhìn toàn cảnh. Câu hỏi của cả phần này là: ai làm gì phía sau màn hình, và công việc chờ ở đâu?

- 🎨 Visual hint: theo deck (slide 25, id `divider-05`).

---

### NUMBERED · What is X · Process Map là gì?
- Kicker: Định nghĩa
- Title: Process Map\n*là gì?*
- On-slide:
  - What: Công việc chuyển qua lại giữa các actor, từ trigger đến kết quả, gồm cả phần user không thấy.
  - Why: Nhìn rõ handoff, phụ thuộc và bottleneck, và tìm bước user không hề cần.
  - When: Khi có hơn một actor, khi flow ổn nhưng user vẫn bị trễ, trước khi bàn giao cho engineering, hoặc để thống nhất ai chịu trách nhiệm bước nào.
- Ví dụ: bản nháp (hoàn tiền: “Đang xử lý” suốt ba ngày)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Khách bấm “Hoàn tiền” và thấy “Đang xử lý” suốt ba ngày. User flow chỉ có ba bước. Vậy đơn đang nằm ở đâu?

  > Process map là công việc chuyển qua lại giữa các actor, từ trigger đến kết quả, gồm cả phần user không thấy. Ở ví dụ này có bốn lane: User, System, Support, Finance, và đơn nằm chờ ở lane Finance. User flow đi theo một người, còn process map cho thấy cả vận hành.

  > Mục tiêu là lộ ra handoff, phụ thuộc, nút thắt cổ chai, và tìm bước tồn tại vì cách tổ chức hoặc hệ thống được xây, không vì user cần.

  > Chúng ta dùng khi có nhiều actor, khi flow ổn mà user vẫn bị trễ hoặc bối rối, trước khi giao cho engineering, và để căn chỉnh design, engineering và ops. Process map không thay thế user flow, nó đặt flow vào bối cảnh.

  > Màn hình không sai. Quy trình mới sai.

- 🎨 Visual hint: theo deck (slide 26, id `pm-what`).

---

### COMPARE · Phạm vi của process map
- Kicker: Phạm vi
- Title: Phạm vi của *process map*
- On-slide: Trong phạm vi | Nhiều actor | Front-stage và back-stage | Từ đầu đến cuối, từ trigger đến kết quả | Ngoài phạm vi | Layout và chi tiết màn hình | Cảm xúc và quyết định của một user | Tóm lại | Cùng task | Cùng flow | Khung nhìn rộng hơn
- Ví dụ: có (ví dụ hoàn tiền ở slide trước)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Ở ví dụ hoàn tiền, process map bàn về điều gì, và không bàn về điều gì?

  > Trong phạm vi: nhiều actor, front-stage và back-stage, và đi từ trigger đến kết quả.

  > Ngoài phạm vi: layout và chi tiết màn hình, cùng cảm xúc và quyết định của một user. Hai thứ này vẫn thuộc user flow, process map không thay thế chúng. Giữ phạm vi này giúp map dễ đọc: nếu map bắt đầu bàn về màn hình, bạn đang lẫn với flow.

  > Tóm lại, cùng task, cùng flow, chỉ là khung nhìn rộng hơn.

- 🎨 Visual hint: theo deck (slide 27, id `pm-scope`).

---

### PROCESS · Cách dựng một process map
- Kicker: Phương pháp
- Title: Cách dựng một\n*process map*
- On-slide: Mỗi mũi tên băng qua lane là một nguy cơ trễ. | 01 | Bắt đầu từ user flow | Các bước của nó trở thành lớp front-stage. | 02 | Liệt kê các actor | User, hệ thống, team nội bộ, bên thứ ba. Mỗi actor một swimlane. | 03 | Đặt mỗi bước vào lane của người sở hữu | Kể cả những bước user không bao giờ thấy. | 04 | Đánh dấu các handoff | Mỗi mũi tên băng qua một lane. Ghi rõ thứ được chuyển đi. | 05 | Tìm các bước chờ, lặp, mồ côi | Bất cứ chỗ nào công việc bị kẹt hoặc lặp vòng. | 06 | So với user flow | Bước nào user chỉ cảm nhận được dưới dạng độ trễ?
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Bắt đầu từ user flow bạn vừa vẽ: các bước của nó trở thành lớp front-stage. Sau đó chúng ta liệt kê các actor, mỗi actor một swimlane.

  > Bước ba là đặt mỗi bước vào lane của người sở hữu, kể cả những bước user không bao giờ thấy. Bước bốn là đánh dấu handoff: mỗi mũi tên băng qua lane, và ghi rõ thứ được chuyển đi.

  > Bước năm là tìm chỗ chờ, lặp, mồ côi. Bước sáu là so với user flow để thấy bước nào user chỉ cảm nhận như độ trễ. Đây là điểm ăn tiền của cả phương pháp.

  > Câu hỏi cho bạn: Bước nào trong flow của bạn mà user chỉ cảm nhận như độ trễ?

- 🎨 Visual hint: theo deck (slide 28, id `pm-build`).

---

### NUMBERED · Các hình của process map
- Kicker: Cấu tạo
- Title: Các hình\n*của process map*
- On-slide: Hai thứ mới so với user flow: hình bình hành và mũi tên handoff. | Swimlane | Mỗi lane một actor: User, System, Ops team, Payment provider | Rectangle | Một hành động của actor đó, ví dụ “Ops team review đặt chỗ” | Diamond | Điểm quyết định, ví dụ “Vượt hạn mức tự động duyệt?” | Parallelogram | Bước tự động của hệ thống: khóa slot, gửi email, kiểm tra thẻ | Handoff arrow | Công việc băng qua các lane, ví dụ System → Ops team: “cần duyệt”
- Ví dụ: có (Ops team review, vượt hạn mức tự động duyệt)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Hãy tự phân loại ba hành động: gửi email xác nhận, Ops review đơn, kiểm tra thẻ. Hành động nào là hình gì?

  > Swimlane là khung chứa mọi thứ, mỗi lane một actor. Rectangle là hành động của actor đó, còn Diamond là quyết định, ví dụ vượt hạn mức tự duyệt hay không.

  > Có hai thứ mới so với user flow. Hình bình hành là bước tự động của hệ thống, và handoff arrow là công việc băng qua các lane.

  > Đáp án: gửi email xác nhận và kiểm tra thẻ là hình bình hành. Ops review đơn là hình chữ nhật trong lane Ops.

- 🎨 Visual hint: theo deck (slide 29, id `pm-shapes`).

---

### DIAGRAM · Đặt và giao đồ ăn
- Kicker: Ví dụ
- Title: Đặt và giao đồ ăn
- On-slide: Khách | App | Nhà hàng | Shipper | Đặt món | Chọn món khác | Nhận món | Gửi đơn | Báo hết món | Theo dõi đơn | Còn món? | Lấy món | NO | YES
- Ví dụ: có (đặt và giao một đơn đồ ăn, bốn lane)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Bạn đặt món, thanh toán xong, rồi nhận tin “món đã hết”. User flow chỉ thấy ba bước. Vậy chuyện gì xảy ra ở giữa?

  > Cùng task, nhưng ở đây có bốn lane: Khách, App, Nhà hàng, Shipper. Chúng ta lần theo handoff từ App sang Nhà hàng: nhà hàng là bên duy nhất biết món còn hay hết. Trong lúc lane Nhà hàng kiểm tra đơn, lane Khách yên lặng, và đó là lúc khách chỉ thấy “đang xử lý”.

  > Cách sửa nằm ở quy trình, không nằm ở màn hình: đồng bộ tồn kho với app, hoặc báo hết món trước khi thanh toán.

  > Câu hỏi cho bạn: Nếu app báo hết món trước khi thanh toán, bao nhiêu đơn không phải huỷ?

- 🎨 Visual hint: SCHEMATIC · theo deck (slide 30, id `pm-example`).

---

### IMAGE · Process flow diagram
- Kicker: Thực tế
- Title: Process flow diagram
- On-slide: Nguồn: aha.io · Process flow diagram template
- Ví dụ: có (process flow diagram mẫu có swimlane, nguồn aha.io)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là một process flow có swimlane. Trong sáu mươi giây, bạn thử tìm các điểm quyết định, rồi tìm chỗ đổi lane.

  > Mỗi lane là một actor, và mỗi mũi tên băng qua lane là một handoff. Sau sáu mươi giây, chúng ta cùng đếm: có bao nhiêu điểm quyết định, mũi tên nào băng qua lane, bước nào user không thấy. Nguồn là template của Aha!, nên đây là template tham khảo chứ không phải dự án của bạn.

  > Nhiều handoff thường nghĩa là nhiều độ trễ.

- 🎨 Visual hint: REAL · theo deck (slide 31, id `pm-real`).

---

### COMPARE · User Flow vs Process Map
- Kicker: So sánh
- Title: User Flow vs *Process Map*
- On-slide: User Flow | Process Map | Góc nhìn | Một user | Cả tổ chức | Câu hỏi | User trải qua những gì? | Ai làm gì, và công việc chờ ở đâu? | Hiển thị | Chỉ front-stage | Front-stage và back-stage | Hình dùng | Pill, Rectangle, Diamond, Arrow, Note | Thêm Swimlane, Parallelogram, Handoff arrow | Thứ tự | Vẽ trước | Vẽ sau, thu nhỏ khung
- Ví dụ: bản nháp (đặt một phần cơm trưa và biết khi nào nó tới)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Chúng ta so sánh hai sơ đồ theo năm dòng. Về góc nhìn, user flow là một user, còn process map là cả tổ chức. Câu hỏi của user flow là user trải qua những gì, còn của process map là ai làm gì và công việc chờ ở đâu. User flow chỉ có front-stage, process map có cả front-stage và back-stage. Về hình, process map dùng thêm swimlane, parallelogram và handoff arrow. Về thứ tự, chúng ta vẽ flow trước, rồi vẽ map sau, thu nhỏ khung.

  > Thử với task “đặt một phần cơm trưa và biết khi nào nó tới”. User flow có sáu bước: mở app, chọn quán, chọn món, thanh toán, theo dõi đơn, nhận hàng. Flow này có vấn đề gì không? Thường bạn sẽ thấy nó ổn và rõ ràng.

  > Process map của cùng task có bốn lane: Khách, App, Quán, Tài xế. Có ba handoff: App sang Quán, Quán sang Tài xế, Tài xế sang App. Màn hình theo dõi chỉ đứng yên khi quán chưa bấm xong hoặc tài xế đang chờ món, và khách chỉ cảm nhận là app chậm. Cách sửa nằm ở quy trình, bằng cách báo “quán đang chuẩn bị” và ước tính thời gian nấu, không phải làm đẹp màn hình theo dõi.

  > Câu hỏi cho bạn: Task của bạn có actor nào mà user không bao giờ thấy, và khi nào bạn dừng ở user flow mà không cần process map?

- 🎨 Visual hint: theo deck (slide 32, id `flow-vs-pm`).

---

### SECTION DIVIDER · AI cho flow
- Num: 06
- Kicker: AI cho flow
- Title: AI cho flow
- Sub: Đầu vào bạn đưa cho AI, và đầu ra bạn kiểm tra trước khi vẽ.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Bạn đã vẽ được user flow và process map bằng tay. Giờ là cách dùng AI mà không để nó bịa ra sản phẩm.

  > Đây là một quy trình làm việc với file, không phải một prompt. Phần này nói về đầu vào bạn đưa cho AI và đầu ra bạn chỉnh trước khi vẽ.

- 🎨 Visual hint: theo deck (slide 33, id `divider-06`).

---

### STATEMENT · Sơ đồ càng đẹp, càng khó nghi ngờ
- Kicker: Vấn đề
- Title: Sơ đồ càng đẹp, *càng khó nghi ngờ*
- On-slide: Bạn hỏi AI | “Vẽ user flow cho việc đổi khung giờ giao.” | AI trả về | Một flow gọn sáu bước. Sản phẩm thật có bảy, vì còn bước xác nhận cut-off. | Cách sửa nằm ở đầu vào bạn đưa cho AI và đầu ra bạn kiểm tra trước khi vẽ.
- Ví dụ: bản nháp (AI vẽ flow đổi khung giờ giao có sáu bước, sản phẩm thật có bảy)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Hỏi AI “vẽ user flow cho việc đổi khung giờ giao” và nó trả về một flow gọn, hợp lý trong vài giây, với sáu bước. Sản phẩm thật có bảy bước, vì còn bước xác nhận cut-off. Nghĩa là sơ đồ đó không gắn với sản phẩm của bạn, và người xem không còn phân biệt được đâu là thật.

  > Sơ đồ càng đẹp thì càng khó nghi ngờ. Vậy làm sao bạn biết bước nào là thật?

  > Cách sửa nằm ở đầu vào bạn đưa cho AI và đầu ra bạn kiểm tra trước khi vẽ.

  > Câu hỏi cho bạn: Làm sao bạn biết bước nào trong một sơ đồ AI vẽ là thật?

- 🎨 Visual hint: theo deck (slide 34, id `ai-problem`).

---

### NUMBERED · Bạn nghĩ trước, AI đến sau
- Kicker: Thứ tự làm việc
- Title: Bạn nghĩ trước,\n*AI đến sau*
- On-slide: Nghiên cứu của Wharton (Nature Human Behaviour, 2025): nhóm brainstorm có AI cho tập ý hẹp hơn nhóm không có AI. | 01 | Bạn viết ý của mình trước | Cây, nhóm thẻ hoặc flow nháp. Rồi mới mở AI. | 02 | AI mở rộng và phản biện | Đổi đầu vào, hỏi “điều ngược lại là gì?”, thay vì xin thêm ý cùng loại. | 03 | Mọi thứ AI đưa ra là hypothesis | Chưa gắn được vào một dòng có nguồn thì chưa đưa vào map.
- Ví dụ: có (nghiên cứu Wharton, Nature Human Behaviour 2025)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Có một nghiên cứu đáng nhớ khi dùng AI để nghĩ ý. Nhóm nghiên cứu ở Wharton, đăng trên Nature Human Behaviour năm 2025, làm năm thí nghiệm brainstorming với một công cụ AI chat. AI nâng mức sáng tạo của từng ý, nhưng nhóm có AI cho tập ý hẹp hơn nhóm không có. Ví dụ trong một bài, ý của nhóm dùng AI trùng nhau tới 94%, còn nhóm không dùng AI thì không ý nào trùng. Đây là nhiệm vụ brainstorming đơn giản, nên chúng ta coi nó là một tín hiệu, chưa phải bằng chứng cho thiết kế sản phẩm thật.

  > Vì vậy thứ tự đúng là bạn nghĩ trước. Bạn viết cây, nhóm thẻ hoặc flow của mình rồi mới mở AI. Nếu hỏi AI trước, câu trả lời của nó thành ý số một và bạn bám theo.

  > Sau khi có ý của mình, AI làm tốt việc mở rộng và phản biện. Hãy đổi đầu vào, ví dụ đưa ràng buộc khác hoặc hỏi “điều ngược lại là gì?”, thay vì xin thêm các ý cùng loại.

  > Cuối cùng, mọi thứ AI đưa ra là hypothesis. Chưa gắn được vào một dòng có nguồn thì chúng ta chưa đưa vào map.

  > Câu hỏi cho bạn: Ở Phần 2 và 3, bạn đã hỏi AI trước hay nghĩ trước?

- 🎨 Visual hint: theo deck (slide 35, id `ai-order`).

---

### DIAGRAM · Bạn và AI thay phiên nhau
- Kicker: Quy trình
- Title: Bạn và AI *thay phiên nhau*
- On-slide: Bạn | AI | Files dự án | đã chốt | File md | (AI nháp) | File md | đã chỉnh | Diagram HTML | (agent) | File md là nguồn sự thật. Diagram chỉ là một cách nhìn vào file.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là cách mình làm, gồm bốn bước. Bạn chỉ AI vào các file đã có: Solution Pool, Opportunities và các file liên quan đến solution đã chốt. AI tạo một file md cho process map.

  > Bạn chỉnh trực tiếp trên file md. Đây là bước quan trọng nhất. Sau đó một agent chuyên vẽ diagram biến file md đã chỉnh thành diagram HTML.

  > File md là nguồn sự thật. Diagram chỉ là một cách nhìn vào file.

- 🎨 Visual hint: SCHEMATIC · theo deck (slide 36, id `ai-process`).

---

### COMPARE · Đưa gì, nhận lại gì
- Kicker: Đầu vào và đầu ra
- Title: Đưa gì, *nhận lại gì*
- On-slide: Đầu vào · bạn chuẩn bị | Files dự án | Solution Pool, Opportunities | Solution đã chốt | Các file liên quan đến solution bạn đã chọn | Yêu cầu | Tạo một file md cho process map | Đầu ra · AI trả về | File md | Các bước theo lane, handoff và chỗ chưa biết | Bạn chỉnh | Sửa trực tiếp trên file md, không sửa trên diagram | Diagram HTML | Agent vẽ từ file md đã chỉnh
- Ví dụ: có (Solution Pool, Opportunities, Solution đã chốt)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Có hai việc cần làm rõ: đưa gì cho AI, và nhận lại gì.

  > Đầu vào là các file bạn đã có từ những buổi trước, không phải một mô tả một dòng: Solution Pool, Opportunities, và các file liên quan đến solution đã chọn. Yêu cầu chỉ có một: tạo file md cho process map.

  > Đầu ra đầu tiên là file md, chưa phải sơ đồ, gồm các bước theo lane, handoff và chỗ chưa biết. Bạn sửa trên file md, không sửa trên diagram. Diagram HTML chỉ được vẽ sau khi bạn chỉnh xong.

- 🎨 Visual hint: theo deck (slide 37, id `ai-io`).

---

### DIAGRAM · Mỗi dòng ghi lane và nguồn
- Kicker: Ví dụ file md
- Title: Mỗi dòng ghi *lane và nguồn*
- On-slide: ID | Lane | Label | Next | Nguồn | Status | S01 | Traveler | Mở app | S02 | Solution đã chốt | stated | S02 | Travel Buddy | Hiện tip ngay, không cần tài khoản | S03 | Solution đã chốt | stated | S03 | Traveler | Muốn lưu tip hoặc nhắn tin? | S04 / S05 | Opportunities | stated | S04 | Traveler | Trả lời ba câu hỏi, đặt kiểm soát vị trí | S06 | Opportunities | stated | S05 | Local | Viết tip | S06 | Solution Pool | stated | S06 | Travel Buddy | Kiểm duyệt tip trước khi hiện | ? | — | unknown | Dòng unknown giữ nguyên cho đến khi bạn tìm được câu trả lời.
- Ví dụ: bản nháp (file md của sản phẩm du lịch, dòng S06 là unknown)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là dạng nội dung bạn nên thấy trong file md. Số liệu là minh họa, lấy theo một sản phẩm du lịch. Mỗi dòng ghi lane, bước tiếp theo và file nguồn.

  > Chúng ta đọc từ S01 đến S05: mỗi bước đều có nguồn từ Solution đã chốt, Opportunities hoặc Solution Pool, và trạng thái stated.

  > Dòng S06 là unknown: các file không nói ai kiểm duyệt tip. AI không được đoán, và đây là câu hỏi bạn mang đi hỏi team. Nếu một file md không có dòng unknown nào thì đó là dấu hiệu đáng ngờ. Dòng unknown giữ nguyên cho đến khi bạn tìm được câu trả lời, và bạn sửa ngay trên file md rồi mới cho agent vẽ.

- 🎨 Visual hint: SCHEMATIC · theo deck (slide 38, id `ai-md`).

---

### IMAGE · Từ file md sang diagram
- Kicker: Kết quả
- Title: Từ file md sang diagram
- On-slide: Ví dụ: process map của một sản phẩm du lịch, do agent vẽ từ file md.
- Ví dụ: có (process map sản phẩm du lịch do agent vẽ từ file md)
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Đây là diagram agent vẽ ra từ file md đã chỉnh, một đoạn Journal của sản phẩm du lịch.

  > Có bốn lane: Traveler, Travel Buddy, Local, Companion / Contact. Hình lục giác là điểm quyết định, nét đứt là nhánh phụ, và những ô viền cam là chỗ chúng ta muốn người xem nhìn vào trước.

  > Mọi bước trong diagram phải có một dòng trong file md. Nếu không có, đó là bước agent tự thêm.

- 🎨 Visual hint: REAL · theo deck (slide 39, id `ai-result`).

---

### DIAGRAM · Một nguồn, nhiều view
- Kicker: Cách nhìn
- Title: Một nguồn, *nhiều view*
- On-slide: Nguồn duy nhất | File md | Mỗi bước một hàng, có nguồn | User flow, cho prototype | Process map, cho process nằm sau màn hình | Đổi nội dung | Sửa một hàng trong file md rồi chạy lại. User flow và process map cùng đổi theo. | Đổi cách hiển thị | Yêu cầu agent đổi thứ tự lane, gộp hoặc tách giai đoạn, hoặc chuyển từ user flow sang process map. File md giữ nguyên. | Không sửa tay trên HTML: lần chạy sau sẽ mất thay đổi đó, và diagram không còn khớp file md.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Một nguồn, nhiều view. File md là nguồn dữ liệu duy nhất. User flow và process map là các cách nhìn do agent vẽ thành HTML từ file md. Chúng ta dùng cách này khi cùng một flow cần hiển thị theo nhiều cách, ví dụ user flow cho prototype và process map cho team phía sau.

  > Có hai kiểu thay đổi. Đổi nội dung là sửa một hàng trong file md rồi chạy lại, và cả hai view đổi theo. Đổi cách hiển thị là yêu cầu agent đổi thứ tự lane, gộp hoặc tách giai đoạn, hoặc chuyển từ user flow sang process map, còn file md giữ nguyên.

  > Quy tắc cho agent chỉ có một: không sửa HTML trực tiếp. Nếu sửa tay thì lần chạy sau sẽ mất thay đổi đó, và diagram không còn khớp file md. Muốn đổi, sửa file md trước rồi vẽ lại. Mỗi bước trên diagram phải có một hàng trong file md.

  > Câu hỏi cho bạn: Flow của bạn hiện có mấy nơi đang giữ cùng một dữ liệu?

- 🎨 Visual hint: SCHEMATIC · theo deck (slide 40, id `ai-views`).

---

### NUMBERED · Ba điểm dừng kiểm tra
- Kicker: Kiểm tra
- Title: Ba điểm dừng *kiểm tra*
- On-slide: A | Sau khi AI tạo file md | Mỗi dòng có ghi nguồn từ file dự án | Mọi dòng unknown còn hiển thị | Dòng không có nguồn chỉ là hypothesis | B | Sau khi bạn chỉnh | Người khác đọc file md có hiểu đúng flow | Lane và handoff đã đúng chưa | C | Sau khi vẽ | Diagram có đúng các bước trong file md | Không có bước nào agent tự thêm | AI không biết ràng buộc thật của hệ thống. Nó có thể đề xuất bỏ một bước mà hệ thống bắt buộc phải có. Hỏi người sở hữu trước.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Mỗi chỗ dừng là một câu hỏi có đáp án có hoặc không.

  > Chỗ A, sau khi AI tạo file md: mỗi dòng có ghi nguồn từ file dự án không, và dòng unknown còn hiển thị không? Dòng nào không có nguồn thì chỉ là hypothesis, câu trả lời không có ID là câu đoán, nên chúng ta chưa đưa vào map.

  > Chỗ B, sau khi bạn chỉnh: người khác đọc file md có hiểu đúng flow không, và lane cùng handoff đã hỏi đúng người chưa?

  > Chỗ C, sau khi vẽ: diagram có đúng các bước trong file md không?

  > AI không biết ràng buộc thật của hệ thống. Nó có thể đề xuất bỏ một bước mà hệ thống bắt buộc phải có, nên bạn hỏi người sở hữu trước.

- 🎨 Visual hint: theo deck (slide 41, id `ai-checks`).

---

### MILESTONE · Vẽ user flow hoặc process map
- Kicker: Activity · 30 phút
- Title: Vẽ *user flow hoặc process map*
- On-slide: 01 | Chọn một trong hai | User flow nếu cần biết user trải qua những gì, process map nếu cần biết ai làm gì phía sau | 02 | Vẽ | Cho Solution của bạn, từ điểm vào đến kết quả, và ghi rõ chỗ có friction | Note | Bạn có thể dùng AI ở bước này.
- Giờ: 30 phút (theo deck)
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Activity 30 phút: bạn vẽ một user flow hoặc một process map cho Solution của bạn.

  > Bạn chọn một trong hai theo câu hỏi cần trả lời, không theo thói quen. Cần biết user trải qua những gì thì vẽ user flow. Cần biết ai làm gì phía sau màn hình thì vẽ process map. Sau đó vẽ từ điểm vào đến kết quả, và ghi rõ chỗ có friction.

  > Bạn có thể dùng AI để làm bước này, theo quy trình ở Phần 6.

- 🎨 Visual hint: theo deck (slide 42, id `activity`).

---

### PRACTICE · User flow hoặc process map
- Kicker: Practice
- Title: *User flow hoặc process map*
- On-slide: User flow | Chọn một task cốt lõi của Solution | Vẽ từ điểm vào đến kết quả, có nhánh lỗi | Ghi chú chỗ có friction | Process map | Bắt đầu từ user flow của task đó | Mỗi actor một swimlane, đánh dấu handoff | Tìm bước user chỉ cảm nhận như độ trễ | Chọn một. Áp dụng vào Solution bạn đã chọn hôm nay, rồi mang kết quả sang buổi sau.
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Bài tập về nhà: bạn hoàn thành một user flow hoặc một process map cho Solution bạn đã chọn hôm nay. Chỉ cần một trong hai, và bạn chọn cái phù hợp với câu hỏi đang cần trả lời.

  > Nếu chọn user flow, bạn chọn một task cốt lõi, vẽ từ điểm vào đến kết quả, có nhánh lỗi, và ghi chú chỗ có friction.

  > Nếu chọn process map, bạn bắt đầu từ user flow của task đó, cho mỗi actor một swimlane, đánh dấu handoff, và tìm bước mà user chỉ cảm nhận như độ trễ.

  > Bạn có thể dùng AI theo quy trình ở Phần 6, và nhớ file md là nguồn chuẩn. Mang kết quả sang buổi sau.

- 🎨 Visual hint: TWO CARDS · theo deck (slide 43, id `homework`).

---

### END · Cấu trúc đúng giúp người dùng tìm được đường, trước khi họ nhìn thấy giao diện.
- Kicker: Takeaway
- Title: Cấu trúc đúng giúp người dùng tìm được đường,\n*trước khi họ nhìn thấy giao diện.*
- On-slide: Winnie Nguyen · nguyenphuctuongvan@gmail.com
- Ví dụ: Không cần.
- Câu hỏi hay gặp: None.
- Speaker notes:

  > Buổi Design làm việc trong cấu trúc chúng ta vừa làm hôm nay, nên bài tập về nhà là điều kiện đầu vào. Chúng ta thống nhất ngày chia sẻ kết quả.

  > Câu hỏi cho bạn: Bạn còn câu hỏi nào không? Cảm ơn bạn.

- 🎨 Visual hint: theo deck (slide 44, id `takeaway`).
