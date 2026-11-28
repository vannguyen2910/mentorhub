# Information Architecture

**Type:** Lesson
**Duration:** 120–135 minutes
**Audience:** Intermediate
**Methods:** Card Sorting · Sitemaps · User Flows · Process Map · AI Workflow for Flows
**Programs:** ui-ux-fundamentals:04, junior-to-mid-level:05
**Slides:** https://claude.ai/artifact/2GcoGVH1bSg29CUWZ1NcY6

---

<!-- **Sync note 2026-11-28 (reverse-sync từ deck Slides mới):** deck mới (https://claude.ai/artifact/2GcoGVH1bSg29CUWZ1NcY6, 44 slide) được dựng lại theo skill slide-deck từ deck Claude Design 42 slide, nên khác cả lesson này lẫn outline cũ. Theo Deck edit rule, deck thắng; cấu trúc dưới đây lấy từ deck mới. Bản trước khi sync: `_archive/information-architecture-lesson-pre-deck-sync-2026-11-28.md` (và bản 2026-10-23). Key Concepts, Practice Activity và Assignment đã viết lại theo deck mới (2026-11-28, tiếng Việt, gửi trực tiếp cho học viên); "Coverage gaps" bên dưới ghi những gì lesson cũ có mà deck không còn. Cấu trúc buổi và coverage gaps: `_review/lesson-structure-and-gaps-2026-11-28.md`. -->

## Key Concepts

### What is Information Architecture?

IA (Information Architecture) là cách tổ chức, đặt tên và sắp xếp nội dung để người dùng tìm được thứ họ cần. IA quyết định ba thứ: cái gì nằm ở đâu, tên gọi là gì, và đi tới đó bằng cách nào.

Ví dụ, một app ngân hàng có các mục Cards, Loans, Savings vì mỗi mục do một team sản phẩm giữ. Khách hàng chỉ hỏi một câu: tiền của tôi đang ở đâu?

Người làm IA thường là UX hoặc Product designer, hoặc IA specialist, cùng PM và content. Họ vẽ sitemap, chạy card sort và tree test, rồi đề xuất cấu trúc. Người quyết định thường là PO, owner của từng mục, hoặc một hệ thống cũ từ nhiều năm trước. Designer đề xuất, owner là người quyết định cuối. Vì vậy một cấu trúc mới cần đủ bằng chứng để thuyết phục owner, không chỉ đẹp trên giấy.

---

### Inherited IA vs Evidence-Based IA

Đây là điểm phân biệt quan trọng nhất của bài. Hầu hết designer nhận một IA có sẵn rồi dùng luôn, không hỏi lại. Cấu trúc đó thường do PO, engineer hoặc stakeholder dựng theo cách *doanh nghiệp* nghĩ: theo tính năng, theo team, theo dòng sản phẩm. Người dùng không tổ chức thông tin theo cách đó.

Ví dụ, cùng một nội dung nhưng chia theo hai cách:

- Inherited: Support, Orders, Account. Ba mục này là ba team.
- Evidence-Based: Đơn của tôi, Sự cố với đơn, Thanh toán. Ba mục này là ba việc khách muốn làm.

| | Inherited IA | Evidence-Based IA |
|---|---|---|
| **Nguồn** | PO, stakeholder, hệ thống cũ | Card sort, tree test, dữ liệu search và support |
| **Logic** | Theo team, theo quyền sở hữu tính năng, theo hệ thống | Theo mental model và task của user |
| **Rủi ro** | “Nghe hợp lý với bên mình” | Cần thời gian và phương pháp |

Inherited không phải lúc nào cũng sai, chỉ là chưa được kiểm chứng. Evidence-Based cũng không phải ý kiến của designer, nên bảng có cột nguồn. Có một cách nhận ra nhanh: nếu một mục chỉ có lý khi bạn nói ra ai sở hữu nó, thì đó là cấu trúc inherited.

---

### Sitemap

**What it is**
Sitemap là sơ đồ mọi màn hình và mục mà user đang chạm vào hôm nay, xếp lồng nhau từ cha đến con, đúng như sản phẩm thật. Sitemap không phải wireframe: nó cho thấy *cái gì tồn tại và nối với nhau thế nào*, không cho thấy trông ra sao.

**Why use it**
- Chưa kiểm kê nội dung thì không viết được bộ thẻ cho card sort.
- Sitemap phơi ra dấu hiệu “sơ đồ tổ chức” (org-chart tell) ngay trên bảng, trước khi bạn có bằng chứng từ user để phản biện.

**When to use it**
- Làm trước card sorting, khi bạn chưa có ý kiến về cách sửa. Nếu đã có ý kiến, bạn sẽ vẽ sitemap thiên lệch.
- Khi bắt đầu một đợt redesign, hoặc khi vào một sản phẩm mới và cần cùng team nhìn một bức tranh hiện trạng.

**How to use it**
Vẽ từ sản phẩm đang chạy, không vẽ từ trí nhớ. Chụp màn hình, đi qua từng màn hình và ghi màn hình cha của nó. Cuối cùng ghi owner cho từng mục cấp 1. Mục nào chỉ giải thích được bằng tên team là dấu hiệu inherited.

Các thẻ của card sort lấy thẳng từ sitemap này. Sau card sort, bạn dựng thêm sitemap thứ hai quanh việc của user, gọi là sitemap evidence-based.

**Ví dụ: Food delivery**
Sitemap của một app giao đồ ăn có năm mục cấp 1: Home, Search, Offers (Growth), Orders (Operations) và Account (Customer Service). Orders có Current, Order detail và Track. Account có Help Centre và Order issues.

Một khách lo vì đơn trễ có hai chỗ để tìm: Track trong Orders, hoặc Order issues trong Account. Hai chỗ đó do hai team giữ. Khách đang lo, còn cấu trúc lại đẩy việc tìm câu trả lời sang nhiều team khác nhau. Đây là bước kiểm kê, không phải phán xét, nên không đổ lỗi cho team nào.

**Ví dụ: Travel Buddy**
Một sitemap do AI dựng từ kết quả card sort: bảy nhóm dưới một app (Onboarding, Dashboard, Discover, Plan / Trip, Connect, Journal / Memories, Profile & Settings). Hai nhóm đầu là lối vào và điểm quay về. Năm nhóm sau là content pillar. Đường cam đánh dấu giả thuyết rủi ro nhất: user có thể gộp Discover và Plan / Trip thành một nhóm.

---

### Card Sorting

**What it is**
Card sorting là phương pháp để biết user nhóm và đặt tên nội dung theo cách nào. User sắp xếp các thẻ (hoặc sticky note) thành nhóm, rồi tự đặt tên cho nhóm.

**Why use it**
Card sort phơi bày mental model của user, thay cho cấu trúc theo team hay hệ thống cũ. Mental model là hình dung sẵn trong đầu user về việc mọi thứ nên nằm ở đâu và gọi là gì. Ví dụ, khách tìm “hoàn tiền” trong Orders, trong khi team đặt nó dưới Help. Người dùng không đọc sitemap của bạn, họ dùng hình dung của chính họ. Card sort cũng cho bạn bằng chứng để bảo vệ quyết định cấu trúc trước stakeholder.

**When to use it**
- Cấu trúc mới hoặc đang bị nghi ngờ.
- Nhãn khó hiểu, hoặc nội dung nhiều và khó nhóm.
- Trước khi thống nhất sitemap.

**Ba định dạng**

| Định dạng | Cách làm | Dùng khi |
|---|---|---|
| **Open** | User tự tạo nhóm và đặt tên | Bạn không tin cấu trúc hiện có. Lộ ra mental model bằng chính lời của họ |
| **Closed** | User sort vào các nhóm bạn đã đặt sẵn | Bạn cần test nhãn. Đây là bài test nhãn, không phải test cấu trúc |
| **Hybrid** | Nhóm của bạn, cộng chỗ để user tự thêm | Bạn muốn tìm chỗ còn thiếu, hợp khi phần lớn cây vẫn ổn |

Hãy chọn định dạng theo câu hỏi bạn cần trả lời: bạn đang cần biết nhóm, hay cần biết nhãn? Ví dụ, một app giao đồ ăn có ba nhóm Orders, Help, Account. Nếu team chưa chắc khách nhóm thế nào thì chạy open. Nếu team chỉ muốn biết tên gọi có dễ hiểu không thì chạy closed. Với dự án nhỏ, bạn có thể bắt đầu bằng open sort 5 người rồi quyết định bước tiếp theo.

**Đọc kết quả: agreement và divergence**
Giả sử 15 người sort thẻ “đồ ăn của tôi bị trễ”: chín người xếp vào nhóm “Nó đang ở đâu”, bốn người vào “Hỗ trợ”, hai người vào “Đơn hàng”. Đây là số minh họa.

- **Agreement** là chỗ nhiều người cùng xếp một nhóm. Chín người đồng ý cho bạn một nhóm rõ, kèm tên nhóm họ đặt.
- **Divergence** là chỗ một thẻ bị rải ra nhiều nhóm. Đây cũng là dữ liệu: khách muốn tìm thẻ đó từ nhiều chỗ, không phải khách sort sai.

Agreement cho bạn biết các nhóm. Divergence cho bạn biết vấn đề nằm ở đâu.

Khi báo kết quả, hãy nói cỡ mẫu ngay câu đầu. Năm người là pilot. Với open sort, khoảng 15 người mới đáng tin.

**Ví dụ: Travel Buddy**
Một card sort do AI dựng từ Solution Pool, gồm năm nhóm: Discover (6 thẻ), Plan / Trip (7), Connect (5), Journal / Memories (5) và Settings / Account (3). Mỗi thẻ là một solution mang ID (D1, P3, C2…) nên truy ngược được nguồn. Đường cam là giả thuyết cần test. Đây là bản nháp của team, chưa phải kết quả của user. Open sort với user thật mới cho biết họ nhóm thế nào.

**Ví dụ: ReferPlus 2019**
Một bài card sort làm trực tiếp trên whiteboard cho một sản phẩm có hai nhóm user là recruiter và headhunter. Đầu ra là cấu trúc navigation và sitemap. Phương pháp tốt, nhưng người tham gia là team nội bộ nên kết quả chỉ phản ánh giả định của team. Để gọi nó là evidence-based, cần chạy lại cùng bài sort với recruiter và headhunter thật, rồi tree test.

---

### User Flows

**What it is**
User flow là sơ đồ các bước một user đi qua để xong một task cụ thể, từ điểm vào đến kết quả. User flow không phải wireframe. Nó vẽ *màn hình, hành động và quyết định* trên đường đi của task, nhìn từ phía user. Ví dụ, flow “Đặt và xác nhận một slot” không vẽ mười màn hình, chỉ vẽ sáu bước và hai điểm quyết định.

**Why use it**
Xác định đường đi của task trước khi vẽ màn hình. Tìm friction (bước user không đáng phải làm) và state còn thiếu (error, empty, loading, success) khi sửa còn rẻ. Phần lớn vấn đề thiết kế nằm ở flow, không nằm ở màn hình: một màn hình có thể rất đẹp mà vẫn nằm sai chỗ trong một flow hỏng.

**When to use it**
- Trước khi wireframe, để thống nhất cấu trúc của task trước khi thiết kế màn hình.
- Khi rà soát sản phẩm cũ, để ghi lại những gì user thật sự phải làm.
- Khi tìm chỗ user bỏ đi hoặc bị lạc.
- Khi bàn giao cho engineering, vì flow cho thấy mỗi màn hình xuất hiện khi nào và trong điều kiện nào.

**Scope**
- **Trong phạm vi:** một user, một task, một điểm vào; màn hình, hành động, quyết định; những gì user nhìn thấy.
- **Ngoài phạm vi:** các actor khác (admin, support, payment provider), việc hệ thống làm phía sau, bàn giao nội bộ. Những phần này thuộc Process Map.

Khi không có user flow, bạn trả ba cái giá: thiết kế màn hình mà không biết trước và sau nó là gì; state lỗi và edge case chỉ lộ ra khi dev; và stakeholder cãi chi tiết màn hình khi chưa thống nhất cấu trúc của task.

**How to draw it**

1. **Đặt khung.** Đặt tên task cụ thể, không phải “checkout” mà là “đặt và xác nhận một slot, user đã dùng app trước đó”. Vẽ pill Start và End trước mọi thứ khác.
2. **Vẽ flow.** Vẽ happy path trước, tức chuỗi bước lý tưởng khi mọi thứ suôn sẻ. Rồi thêm nhánh lỗi và edge case (slot đã bị lấy, chưa đăng nhập, empty state). Mỗi nhánh đều phải có đích, không để mũi tên treo. Cuối cùng ghi chú chỗ có friction và ghi rõ nó tốn gì.
3. **Kiểm tra.** Mỗi diamond có hai mũi tên ra, đều có nhãn. Không để hình nào bị bỏ lẻ.

**Năm hình mang toàn bộ ý nghĩa**

| Hình | Ý nghĩa | Ví dụ |
|---|---|---|
| **Pill** | Điểm bắt đầu và kết thúc | “User mở app”, “Đã xác nhận đặt chỗ” |
| **Rectangle** | Một màn hình hoặc hành động của user | Xem danh sách slot, bấm “Pay” |
| **Diamond** | Điểm quyết định, có đúng hai mũi tên ra | “Slot còn trống không?”, “Thanh toán thành công?” |
| **Arrow** | Hướng đi của flow, gắn nhãn cho nhánh | Yes / No, Success / Error |
| **Note** | Ngữ cảnh không nhét vừa một hình | “Friction: phải bấm 3 lần mới tới đây” |

Dùng hình nhất quán thì cả team đọc được flow mà không cần giải thích. Nếu bạn cần hình thứ sáu, đó thường là một bước của hệ thống, tức là chuyện của Process Map.

**Ví dụ: Đặt và xác nhận một slot**
Start → xem danh sách slot → chọn slot → ◇ Slot còn trống? (No → quay lại danh sách slot) → xem lại đặt chỗ → thanh toán → ◇ Thanh toán OK? (No → lỗi, thử lại hoặc đổi phương thức) → đã xác nhận → End.

Ở bước cuối, màn hình xác nhận hiện “pending”, không phải “confirmed”. Flow chỉ cho thấy những gì user thấy, nên không giải thích được vì sao lại hiện “pending”. Câu trả lời nằm ở phần Process Map.

**Ba điều một flow cho bạn thấy**
- Điểm quyết định bắt user làm việc mà hệ thống có thể tự xử lý.
- Flow dài hơn mức cần thiết vì nội dung nằm sai chỗ trong IA.
- Thiếu state: empty, error, loading, success.

Một task cốt lõi mà dài hơn bảy bước thì nhiều khả năng lỗi nằm ở IA, không phải ở thiết kế màn hình.

**Đánh giá từng bước bằng JTBD**
JTBD (Jobs-to-Be-Done) cho bạn một cách đọc flow: với mỗi bước, hãy hỏi bước này giúp user tiến gần job của họ, hay chỉ là friction do hệ thống tự tạo ra. Ví dụ, với job “tôi muốn biết đơn có tới kịp trước 7 giờ không”, hệ quả cho flow là hiển thị giờ dự kiến ngay ở màn hình đầu tiên, không bắt user bấm vào từng đơn.

| JTBD insight | Hệ quả cho flow |
|---|---|
| User cần xác nhận nhanh trước khi mất slot | Không đặt màn hình upsell trên đường đi chính |
| User lo lắng về những hành động không thể hoàn tác | Thêm bước review trước khi xác nhận cuối cùng |
| User muốn trông chuyên nghiệp khi chia sẻ sản phẩm của mình | Đặt “share” ngay lúc hoàn thành task, đừng giấu trong settings |

Mỗi cặp nhu cầu của user và hệ quả cho flow là một quyết định thiết kế.

---

### Process Map

**What it is**
Process map là sơ đồ cho thấy công việc chuyển qua lại giữa các actor (user, hệ thống, team nội bộ và bên thứ ba) từ trigger cho đến khi ra kết quả. User flow đi theo đường của một người. Process map cho thấy toàn bộ vận hành phía sau, kể cả phần user không bao giờ nhìn thấy.

Ví dụ, khách bấm “Hoàn tiền” và thấy “Đang xử lý” suốt ba ngày. User flow chỉ có ba bước. Process map có bốn lane: User, System, Support, Finance, và đơn nằm chờ ở lane Finance. Màn hình không sai. Quy trình mới sai.

**Why use it**
Nhìn rõ chỗ bàn giao (handoff), chỗ phụ thuộc lẫn nhau và chỗ nghẽn (bottleneck). Từ đó tìm ra những bước chỉ có vì cách tổ chức hoặc hệ thống được dựng, chứ user không hề cần.

**When to use it**
- Task có hơn một actor: checkout qua payment provider, onboarding có email hệ thống, tính năng admin.
- User flow trông ổn nhưng user vẫn bị trễ hoặc bối rối, và màn hình không giải thích được.
- Trước khi bàn giao cho engineering, để cho thấy logic back-stage phía sau mỗi màn hình.
- Khi cần thống nhất giữa design, engineering và operations về việc ai chịu trách nhiệm bước nào.

**Scope**
- **Trong phạm vi:** nhiều actor; front-stage và back-stage; từ đầu đến cuối, từ trigger đến kết quả.
- **Ngoài phạm vi:** layout và chi tiết màn hình; cảm xúc và quyết định của một user. Hai thứ này vẫn thuộc user flow.

Cùng task, cùng flow, chỉ là khung nhìn rộng hơn. Nếu map bắt đầu bàn về màn hình, bạn đang lẫn với flow.

**How to build it**

1. **Bắt đầu từ user flow.** Các bước của nó trở thành lớp front-stage.
2. **Liệt kê các actor.** User, hệ thống, team nội bộ, bên thứ ba. Mỗi actor một swimlane.
3. **Đặt mỗi bước vào lane của người sở hữu**, kể cả những bước user không bao giờ thấy.
4. **Đánh dấu các handoff.** Mỗi mũi tên băng qua một lane là một handoff. Ghi rõ thứ được chuyển đi.
5. **Tìm các bước chờ, lặp và mồ côi**, tức bất cứ chỗ nào công việc bị kẹt hoặc lặp vòng.
6. **So với user flow.** Bước nào user chỉ cảm nhận được dưới dạng độ trễ? Đây là điểm đáng giá nhất của cả phương pháp.

Mỗi mũi tên băng qua lane là một nguy cơ trễ.

**Các hình của process map**
Process map dùng lại năm hình của user flow, thêm hai thứ mới: hình bình hành và mũi tên handoff.

| Hình | Ý nghĩa | Ví dụ |
|---|---|---|
| **Swimlane** | Mỗi lane một actor | User, System, Ops team, Payment provider |
| **Rectangle** | Một hành động của actor đó | “Ops team review đặt chỗ” |
| **Diamond** | Điểm quyết định | “Vượt hạn mức tự động duyệt?” |
| **Parallelogram** | Bước tự động của hệ thống | Khóa slot, gửi email, kiểm tra thẻ |
| **Handoff arrow** | Công việc băng qua các lane | System → Ops team: “cần duyệt” |

**Ví dụ: Đặt và giao đồ ăn**
Bạn đặt món, thanh toán xong, rồi nhận tin “món đã hết”. User flow chỉ thấy ba bước. Process map của cùng task có bốn lane: Khách, App, Nhà hàng, Shipper. Handoff từ App sang Nhà hàng là chỗ quyết định: nhà hàng là bên duy nhất biết món còn hay hết. Trong lúc lane Nhà hàng kiểm tra đơn, lane Khách yên lặng, và đó là lúc khách chỉ thấy “đang xử lý”.

Cách sửa nằm ở quy trình, không nằm ở màn hình: đồng bộ tồn kho với app, hoặc báo hết món trước khi thanh toán.

**Quay lại câu hỏi “pending”**
Ở ví dụ đặt slot, màn hình hiện “pending” vì đơn vượt hạn mức tự duyệt và đang chờ Ops team. Màn hình không có lỗi, quy trình phía sau mới là nguyên nhân. Cách sửa là tự động duyệt dưới một hạn mức và hiển thị trạng thái duyệt cho user.

**User Flow vs Process Map**

| | User Flow | Process Map |
|---|---|---|
| **Góc nhìn** | Một user | Cả tổ chức |
| **Câu hỏi** | User trải qua những gì? | Ai làm gì, và công việc chờ ở đâu? |
| **Hiển thị** | Chỉ front-stage | Front-stage và back-stage |
| **Hình dùng** | Pill, Rectangle, Diamond, Arrow, Note | Thêm Swimlane, Parallelogram, Handoff arrow |
| **Thứ tự** | Vẽ trước | Vẽ sau, thu nhỏ khung |

Hãy dừng ở user flow khi task chỉ có một actor và friction nằm trong các màn hình. Thêm process map khi friction không giải thích được bằng màn hình.

---

### AI cho flow

**What it is**
Đây là một quy trình làm việc với file để dùng AI vẽ user flow hoặc process map mà không để AI bịa ra sản phẩm. Nó không phải một prompt. Đầu vào là các file dự án bạn đã có, đầu ra là một file md bạn kiểm tra và chỉnh trước khi vẽ.

**Why not just one prompt?**
Nếu bạn hỏi AI “vẽ user flow cho việc đổi khung giờ giao”, nó trả về một flow gọn và hợp lý trong vài giây, với sáu bước. Sản phẩm thật có bảy bước, vì còn bước xác nhận cut-off. Sơ đồ đó không gắn với sản phẩm của bạn, và sơ đồ càng đẹp thì càng khó nghi ngờ. Cách sửa nằm ở đầu vào bạn đưa cho AI và đầu ra bạn kiểm tra trước khi vẽ.

**Bạn nghĩ trước, AI đến sau**
Nhóm nghiên cứu của Wharton (Meincke, Nave và Terwiesch, *Nature Human Behaviour*, 2025) làm năm thí nghiệm brainstorming với một công cụ AI chat. AI nâng mức sáng tạo của từng ý, nhưng nhóm có AI cho tập ý hẹp hơn nhóm không có AI. Trong một bài, ý của nhóm dùng AI trùng nhau tới 94%, còn nhóm không dùng AI thì không có ý nào trùng. Đây là nhiệm vụ brainstorming đơn giản, nên hãy xem nó là một tín hiệu, chưa phải bằng chứng cho thiết kế sản phẩm thật.

Từ đó có thể suy luận rằng nếu hỏi AI trước, câu trả lời của nó thành ý số một và bạn bám theo. Vì vậy:

1. **Bạn viết ý của mình trước.** Cây, nhóm thẻ hoặc flow nháp. Rồi mới mở AI.
2. **AI mở rộng và phản biện.** Đổi đầu vào (thêm một ràng buộc khác, hỏi “điều ngược lại là gì?”) thay vì xin thêm các ý cùng loại.
3. **Mọi thứ AI đưa ra là hypothesis.** Chưa gắn được vào một dòng có nguồn thì chưa đưa vào map.

**Quy trình: bạn và AI thay phiên nhau**

| # | Bước | Ai làm | Kết quả |
|---|---|---|---|
| 1 | Chỉ AI vào các file dự án đã chốt: Solution Pool, Opportunities và các file liên quan đến solution bạn đã chọn | Bạn | Đầu vào |
| 2 | Tạo một file md cho process map | AI | File md (bản nháp của AI) |
| 3 | Chỉnh trực tiếp trên file md. Đây là bước quan trọng nhất | Bạn | File md đã chỉnh |
| 4 | Vẽ diagram HTML từ file md đã chỉnh | Agent | Diagram HTML |

File md là nguồn sự thật. Diagram chỉ là một cách nhìn vào file.

**Đưa gì, nhận lại gì**
- **Đầu vào:** các file bạn đã có từ những buổi trước, không phải một mô tả một dòng. Yêu cầu chỉ có một: tạo file md cho process map.
- **Đầu ra đầu tiên:** file md, chưa phải sơ đồ. File gồm các bước theo lane, handoff và những chỗ chưa biết. Bạn sửa trên file md, không sửa trên diagram.

**Một dòng trong file md trông thế nào**
Mỗi dòng ghi ID, lane, label, bước tiếp theo, nguồn và status (stated, inferred hoặc unknown). Ví dụ minh họa lấy theo một sản phẩm du lịch:

| ID | Lane | Label | Next | Nguồn | Status |
|---|---|---|---|---|---|
| S01 | Traveler | Mở app | S02 | Solution đã chốt | stated |
| S02 | Travel Buddy | Hiện tip ngay, không cần tài khoản | S03 | Solution đã chốt | stated |
| S03 | Traveler | Muốn lưu tip hoặc nhắn tin? | S04 / S05 | Opportunities | stated |
| S06 | Travel Buddy | Kiểm duyệt tip trước khi hiện | ? | — | unknown |

Dòng S06 là unknown vì các file không nói ai kiểm duyệt tip. AI không được đoán, và đây là câu hỏi bạn mang đi hỏi team. Một file md không có dòng unknown nào là dấu hiệu đáng ngờ. Dòng unknown giữ nguyên cho đến khi bạn tìm được câu trả lời.

**Một nguồn, nhiều view**
File md là nguồn dữ liệu duy nhất. User flow và process map là các cách nhìn do agent vẽ thành HTML từ file md. Cách này hữu ích khi cùng một flow cần hiển thị theo nhiều cách, ví dụ user flow cho prototype và process map cho team phía sau.

- **Đổi nội dung:** sửa một hàng trong file md rồi chạy lại. User flow và process map cùng đổi theo.
- **Đổi cách hiển thị:** yêu cầu agent đổi thứ tự lane, gộp hoặc tách giai đoạn, hoặc chuyển từ user flow sang process map. File md giữ nguyên.
- **Quy tắc cho agent:** không sửa HTML trực tiếp. Lần chạy sau sẽ mất thay đổi đó, và diagram không còn khớp file md. Mỗi bước trên diagram phải có một hàng trong file md.

**Ba điểm dừng kiểm tra**
Mỗi điểm dừng là một câu hỏi có đáp án có hoặc không.

| Điểm | Khi nào | Câu hỏi kiểm tra |
|---|---|---|
| **A** | Sau khi AI tạo file md | Mỗi dòng có ghi nguồn từ file dự án không? Mọi dòng unknown còn hiển thị không? Dòng không có nguồn chỉ là hypothesis |
| **B** | Sau khi bạn chỉnh | Người khác đọc file md có hiểu đúng flow không? Lane và handoff đã đúng chưa? |
| **C** | Sau khi vẽ | Diagram có đúng các bước trong file md không? Có bước nào agent tự thêm không? |

**Watch out for**
- AI không biết ràng buộc thật của hệ thống. Nó có thể đề xuất bỏ một bước mà hệ thống bắt buộc phải có. Hãy hỏi người sở hữu trước.
- Một sơ đồ sạch và không có dòng unknown nào là dấu hiệu đáng ngờ, vì dữ liệu thật luôn có chỗ còn thiếu.
- Kết quả của AI trông rất đáng tin. Hãy đếm số bước trên diagram và đối chiếu với file md.

**What this cannot tell you:** vì sao user bỏ đi, các bước thật sự mất bao lâu, hay cách sửa có hiệu quả không. Muốn biết những điều đó, bạn cần làm việc với user thật.

---

## Tools & Materials

- Solution bạn đã chọn trong các buổi trước, kèm các file dự án: Solution Pool, Opportunities và các file liên quan.
- FigJam hoặc Miro để vẽ user flow và process map.
- Ảnh chụp màn hình của các màn hình có trong flow.
- JTBD map từ buổi trước, để chọn task cần vẽ.

---

## Practice Activity — Vẽ user flow hoặc process map · 30 min

Bạn vẽ một user flow hoặc một process map cho Solution của mình, từ điểm vào đến kết quả.

**Steps:**

1. **Chọn một trong hai** theo câu hỏi bạn cần trả lời, không theo thói quen.
   - **User flow** nếu bạn cần biết user trải qua những gì.
   - **Process map** nếu bạn cần biết ai làm gì phía sau màn hình.
2. **Chọn task.** Lấy một task cốt lõi từ JTBD map, đặt tên cụ thể: không phải “mua hàng” mà là “tìm và lưu một sản phẩm để xem lại”.
3. **Vẽ từ điểm vào đến kết quả.**
   - User flow: Start và End trước, happy path, rồi một nhánh lỗi cho mỗi diamond.
   - Process map: bắt đầu từ user flow của task đó, mỗi actor một swimlane, thêm các bước back-stage và đánh dấu mọi handoff.
4. **Ghi rõ chỗ có friction.** Đánh dấu bước dài, bước gây bất ngờ, hoặc bước user chỉ cảm nhận như độ trễ.

Bạn có thể dùng AI ở bước này, theo quy trình ở phần AI cho flow.

**Debrief prompts:**
- Bước nào làm bạn bất ngờ, tức bước bạn không nhận ra là có cho đến khi vẽ?
- Điểm quyết định nào hệ thống có thể tự xử lý, để bỏ hẳn một bước?
- Vấn đề nào hóa ra là vấn đề của quy trình, không phải của màn hình?

---

## Assignment (before next session)

Hoàn thành **một** user flow hoặc **một** process map cho Solution bạn đã chọn hôm nay. Chọn cái phù hợp với câu hỏi đang cần trả lời.

- **User flow:** chọn một task cốt lõi của Solution. Vẽ từ điểm vào đến kết quả, có nhánh lỗi. Ghi chú chỗ có friction.
- **Process map:** bắt đầu từ user flow của task đó. Mỗi actor một swimlane, đánh dấu handoff. Tìm bước mà user chỉ cảm nhận như độ trễ.

Bạn có thể dùng AI theo quy trình ở phần AI cho flow. Hãy nhớ file md là nguồn chuẩn, và diagram luôn được vẽ lại từ file md. Mang kết quả sang buổi sau.

---

## Related Notion Resources

- [Design Activities by DT Stage — Reference](https://www.notion.so/3248a6b135db810385bdf06991f4f87a) — Card sorting and tree testing in context of the full DT cycle
- [Session 1 Playback — Design Thinking in Practice](https://www.notion.so/3318a6b135db81a2a1ebf83b4ec081a5) — "Organise for users — Evidence-based sitemap, Task flows"
- [Progress Tracker](https://www.notion.so/3238a6b135db816db041d2cfbc58fa8c) — Evidence-based sitemap is the S4 artifact

---

*Lesson: Information Architecture · Part of the 8-session UX Mentoring Program*
