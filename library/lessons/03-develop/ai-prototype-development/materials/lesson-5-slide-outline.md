---
title: "Lesson 5: Reuse What Others Built"
lesson_file: "lesson-5-reuse-what-others-built.md"
level: "intermediate"
slide_count: 25
duration: "90 min"
status: deck-built
built_deck: "../slides/Lesson 5 - Reuse What Others Built.dc.html"
last_synced: 2026-10-18
---

> **Source of truth:** `lesson-5-reuse-what-others-built.md`
> Mọi thay đổi về activity, timing và concept được làm ở file lesson trước, rồi phản ánh sang đây. File này chỉ chứa phần riêng của slide: layout, on-slide text, visual hint, kicker và speaker notes.
> **Layout lấy đúng 13 loại trong `_system/rules/slide-deck-rules.md`.** Không dùng `SECTION`, `COMPARISON`, `ACTIVITY`.
> **Speaker notes là bullet tiếng Việt**, giọng "mình". Tiêu đề, Kicker và nhãn bằng tiếng Anh. Không ghi thời lượng trên slide, trừ slide `MILESTONE`.
> **Không ghi tên tool AI hay tên mentee trên slide và trong notes.** Ảnh chụp màn hình được giữ nguyên tên trong ảnh theo quyết định ngày 2026-10-17. Bộ ảnh nằm trong `../assets/` (tiền tố `lesson-5-`).

---

## Session metadata

| Field | Value |
|---|---|
| Program | private-training |
| Track / session | Lesson 5 (extra bonus) |
| Stage | Develop |
| Prior session | Lesson 4: Publish It |
| Next session | Không có (bài cuối của arc) |
| Running example | Một template repo công khai được clone vào folder mới, rồi chỉnh thành dự án của học viên |
| Deck file | `slides/Lesson 5 - Reuse What Others Built.dc.html` |

## Slide structure — 25 slides

| # | Block | Slides | Minutes |
|---|---|---|---|
| 0 | Open | 3 | 5 |
| 1 | Theory | 9 | 30 |
| 2 | Bridge | 2 | 5 |
| 3 | Practice | 4 | 30 |
| 4 | Bonus | 5 | 10 |
| 5 | Close | 2 | 5 |

- Arc: **Open** → **Theory** → **Bridge** → **Practice** → **Bonus** → **Close**. Tổng 85 phút, đệm 5 phút.
- Section dividers đánh dấu các bước chuyển lớn: **Theory**, **Practice** và **Bonus** (Bonus đổi chủ đề). Các phần bên trong Theory được đánh dấu bằng kicker.
- Bridge là một `MILESTONE` (`Num:` = 5) và một `DIAGRAM` Cheat sheet ở lại trên màn hình suốt Practice.
- Practice là một `MILESTONE` (`Num:` = 30) và một `PROCESS` làm task card. Practice liền mạch, không quay lại dạy giữa chừng.
- Theory 30 phút, 4 phần, mỗi phần kết thúc bằng một câu kiểm tra 30 giây hỏi miệng (nằm trong notes, không phải slide riêng).
- Bonus 10 phút nằm trong 90 phút, sau Practice để không ngắt Practice.

---

## Slides

### COVER
- Year: 2026 · Winnie Nguyen
- Stage: Develop
- Title: Reuse What\n*Others Built*
- Subtitle: Dùng lại skill và repo của người khác mà không cần code.
- Author: Winnie Nguyen
- Credentials:
  - Senior Product Designer at NAB
  - Master of UX & Service Design
  - Product Design Instructor
- Right panel photo: ảnh thật, một designer làm việc với laptop, ánh sáng ấm, không lộ màn hình.
- Speaker notes:
  - Mở bằng một câu hỏi: lần gần nhất mình làm một việc lặp lại, có ai đó đã làm sẵn chưa?
  - Nói trước giới hạn của buổi học: mình không đọc code, nên bài này dạy cách chọn, thử an toàn và chỉnh bằng file markdown.
  - Giới thiệu đây là bài extra bonus, nối tiếp Lesson 4: repo đã publish được, giờ học dùng repo của người khác.
- 🎨 Visual hint: Cover layout, fixed. White left panel with year line, stage label, title (accent on line 2) and subtitle. Right panel is the real photo with dark gradient overlay, name and three credential lines bottom-left.

---

## 0. Open

### STATEMENT · Someone Already Built It
- Kicker: A real story
- Title: Ai đó đã làm\nrồi
- On-slide: Một designer cần diagram có styling và complex diagram. Các creator trên mạng xã hội đang dùng một skill làm được.
- Speaker notes:
  - Kể câu chuyện thật: mình cần vẽ diagram có styling và complex diagram, thấy creator trên TikTok và YouTube dùng một skill làm rất đẹp
  - Mình lần ra repo công khai của skill đó, đọc README, rồi nhờ AI coding tool cài vào
  - Cài ở phạm vi dùng chung cho mọi dự án, hoặc chỉ cho một dự án
  - Về sau cần vẽ diagram thì gọi skill bằng tên, không phải dựng lại từ đầu
  - **Câu chuyển:** trong dự án của bạn, việc nào lặp lại mà có thể đã có người làm rồi? Học viên nêu một việc, dùng lại ở phần Theory
- 🎨 Visual hint: TYPOGRAPHIC. Một câu lớn ở giữa, `em` ở "đã làm" màu sienna. Không có ảnh.

---

### IMAGE · What the Skill Produced
- Kicker: The result
- Title: Kết quả của một skill vẽ diagram
- On-slide: User flow swimlane dựng bằng một diagram skill, từ demo case Travel Buddy.
- Speaker notes:
  - Cho xem kết quả thật của skill trong câu chuyện: một user flow có swimlane, các giai đoạn getting started, discover và plan, và bốn lane traveler, app, local, companion
  - Chỉ ra ba thứ mà tự vẽ tay mất nhiều thời gian: lane phân vai, nhánh quyết định có nhãn YES và NO, và màu nhấn một bước quan trọng
  - Ví dụ: một designer có một flow dài mười lăm bước, nhờ skill dựng lại trong vài phút rồi chỉnh nhãn, thay vì căn từng khung trong file design
  - Skill không thay người thiết kế flow. Mình vẫn là người quyết định bước nào có mặt và bước nào là điểm đau
  - Trong dự án của bạn, flow nào đang cần vẽ lại mà bạn thấy ngại làm tay?
- 🎨 Visual hint: REAL. Ảnh `../assets/lesson-5-showcase-user-flow-swimlane.webp`, full bleed, giữ nguyên chữ trong ảnh.

---

## 1. Theory

### SECTION DIVIDER · Theory
- Kicker: Theory
- Title: Chọn, đọc, dùng\n*lại*
- Sub: Bốn thứ dùng lại được, nơi tìm, cách đọc, ba cách dùng.
- Speaker notes:
  - Giới thiệu bốn phần của Theory, không có activity nào trong block này
  - Mỗi phần kết thúc bằng một câu hỏi miệng 30 giây, không phải bài tập
  - Mọi khái niệm trong phần này đều được dùng lại ở Practice
- 🎨 Visual hint: SECTION DIVIDER layout, `--paper-deeper` background. Số lớn `.num` 120px, title 144px.

### NUMBERED · Four Things You Can Reuse
- Kicker: Four things
- Title: Bốn thứ dùng lại được
- On-slide:
  - 1 · Skill: folder có file SKILL.md, AI đọc và làm theo khi được gọi.
  - 2 · Template repo: repo mẫu có folder và quy trình dựng sẵn.
  - 3 · Component library: bộ component chép vào dự án.
  - 4 · File rules: một hai file markdown chứa luật cho AI.
- Speaker notes:
  - Skill là folder có file `SKILL.md` gồm tên, mô tả và hướng dẫn, kèm script nếu cần. Nội dung chính là markdown, nên mình đọc và chỉnh được mà không cần viết code
  - Ví dụ skill: một skill vẽ diagram theo một style cố định, gọi bằng tên khi cần
  - Ví dụ template repo: một workspace cho cả quy trình design, bấm "Use this template" là có bản của mình
  - Ví dụ file rules: file luật đặt tên và giọng văn mình đã viết ở các bài trước
  - **Kiểm tra (30 giây):** với việc lặp lại bạn vừa nêu, loại nào phù hợp nhất?
  - Chuyển ý: loại nào cũng phải tìm được trước đã
- 🎨 Visual hint: NUMBERED layout, 2-col grid, bốn item với số 72px sienna.

### NUMBERED · Where to Look
- Kicker: Three places
- Title: Ba nơi để tìm
- On-slide:
  - 1 · GitHub search: gõ nhu cầu bằng tiếng Anh, lọc theo sao và lần cập nhật.
  - 2 · Awesome list: danh sách tuyển chọn do người khác duy trì.
  - 3 · Trang riêng của tool: mỗi tool có chỗ liệt kê skill của nó.
- Speaker notes:
  - GitHub search: gõ nhu cầu như "user journey skill", rồi lọc theo số sao và lần cập nhật gần nhất
  - Awesome list: danh sách tuyển chọn trên GitHub, đã được người duy trì lọc một lần, nên dễ cho người mới
  - Mạng xã hội thường là nơi mình thấy skill lần đầu. Khi đó cần lần ra repo gốc, không cài từ link trong bài đăng
  - Ví dụ: thấy một creator khoe skill, mình tìm tên repo trong mô tả, rồi mở trang repo gốc trên GitHub
  - Trong dự án của bạn, thử tìm một việc lặp lại bằng hai nguồn ngay bây giờ nếu còn thời gian
- 🎨 Visual hint: NUMBERED layout, 3-col override.

### IMAGE · GitHub Marketplace Lists Apps, Not Skills
- Kicker: A common mix-up
- Title: Marketplace không phải\nnơi tìm skill
- On-slide: GitHub Marketplace liệt kê Apps và Actions. Skill nằm ở repo và awesome list.
- Speaker notes:
  - Nhiều người tưởng GitHub Marketplace có mục skill, thực ra chỉ có Apps và Actions
  - Skill được tìm bằng GitHub search, awesome list hoặc trang riêng của từng tool `[to confirm]`
  - Nói rõ để học viên không mất thời gian tìm sai chỗ
  - Ví dụ: một designer mở Marketplace gõ "diagram skill" và không thấy gì, rồi nghĩ là chưa có ai làm
  - Chuyển ý: tìm ra repo rồi, đọc trang repo thế nào?
- 🎨 Visual hint: REAL. Ảnh chụp `../assets/lesson-5-github-marketplace-home.webp`, full bleed, không chú thích.

### IMAGE · Read the Repo Page
- Kicker: Signals
- Title: Đọc trang repo trước khi cài
- On-slide: Tác giả, số sao, commit gần nhất, license, README.
- Speaker notes:
  - Chỉ vào từng dấu hiệu trên ảnh: tác giả, số sao và fork, commit gần nhất, license ở cột About, README bên dưới
  - Ví dụ: repo này có hơn năm mươi nghìn sao, license MIT, commit cách đây vài giờ, nên vừa được quan tâm vừa còn được bảo trì
  - Số sao là tín hiệu quan tâm, không phải bằng chứng an toàn
  - **Kiểm tra (30 giây):** repo 200 sao, commit cuối cách đây hai năm, không có license. Dấu hiệu nào đáng lo nhất?
  - Trong dự án của bạn, mở một repo bạn đang quan tâm và đọc năm dấu hiệu này
- 🎨 Visual hint: REAL. Ảnh chụp `../assets/lesson-5-repo-page-signals.png`, giữ nguyên tên trong ảnh. Có thể khoanh năm vùng bằng số 1 đến 5 màu sienna.

### STATEMENT · Stars Are Interest, Not Safety
- Kicker: A caution
- Title: Nhiều sao chưa chắc\n*an toàn*
- On-slide: Nghiên cứu của các hãng bảo mật tìm thấy lỗ hổng trong nhiều skill được dùng rộng rãi.
- Speaker notes:
  - Một nghiên cứu phân tích 31.132 skill, thấy 26,1% có ít nhất một lỗ hổng `[to confirm]`
  - Snyk quét gần 4.000 skill, 13,4% có vấn đề nghiêm trọng `[to confirm]`
  - ESET cảnh báo chỉ dẫn độc hại có thể nằm ngay trong README và các tài liệu AI đọc `[to confirm]`
  - Nói rõ: đây là nghiên cứu của hãng bảo mật, phương pháp mỗi nơi một khác, không so sánh trực tiếp được
  - Ví dụ: một skill có nhiều sao nhưng file hướng dẫn có một dòng yêu cầu gửi nội dung folder ra ngoài, và người dùng không đọc tới
  - Chuyển ý: mình không đọc code, nên cần cách khác để đọc
- 🎨 Visual hint: TYPOGRAPHIC. Câu lớn ở giữa, `em` màu sienna, một dòng nguồn nhỏ ở dưới.

### PROCESS · Read Without Reading Code
- Kicker: Method
- Title: Đọc mà không\ncần đọc code
- On-slide:
  - 1 · Mình tự xem README và ảnh, viết dự đoán ba dòng.
  - 2 · Đưa README và file markdown cho AI chat tool.
  - 3 · Hỏi làm gì, đụng file nào, rồi nhờ chấm độ tin cậy và an toàn.
  - 4 · Đối chiếu với dự đoán, ghi chỗ lệch và chỗ AI không chắc.
- Speaker notes:
  - Thứ tự quan trọng: tự viết dự đoán trước, rồi mới nhờ AI diễn giải. Làm ngược lại thì dự đoán bị AI định hướng
  - Câu hỏi cho AI: repo làm gì, cho ai, đầu ra là gì, mỗi file markdown chỉ dẫn gì, có chỉ dẫn nào chạy lệnh, xoá hoặc gửi dữ liệu ra ngoài không
  - Yêu cầu AI tách "điều có trong file" và "điều suy đoán"
  - Sau diễn giải, nhờ AI chấm độ tin cậy và an toàn theo bộ câu hỏi cố định, kèm căn cứ trích từ file. Chiếm khoảng hai phút, lấy từ phần đệm
  - Điểm chấm chỉ là ý kiến tham khảo: AI chấm dựa trên chính file nó đọc, nên không thay được các dấu hiệu bên ngoài
  - **Nói rõ giới hạn:** AI nói "an toàn" vẫn chưa phải là an toàn. Đây là một lớp kiểm tra, không phải lớp duy nhất
  - **Kiểm tra (30 giây):** AI nói "repo này an toàn". Câu đó nên được hiểu thế nào?
  - Ví dụ: một designer nhờ AI diễn giải README và thấy AI không nhắc tới một file hướng dẫn thứ hai, nhờ vậy phát hiện thêm một chỉ dẫn chưa đọc
- 🎨 Visual hint: SCHEMATIC. Process 4 bước ngang, bước 1 và 4 đánh dấu "mình", bước 2 và 3 đánh dấu "AI".

### NUMBERED · Three Ways to Reuse
- Kicker: Three ways
- Title: Ba cách dùng lại
- On-slide:
  - 1 · Dùng nguyên bản khi repo làm đúng việc cần.
  - 2 · Lấy làm template khi cấu trúc đúng, nội dung khác.
  - 3 · Chỉnh file markdown khi gần đúng, cần khác vài chỗ.
- Speaker notes:
  - Dùng nguyên bản: clone hoặc cài, rồi dùng luôn
  - Lấy làm template: giữ cấu trúc, thay nội dung bằng dự án của mình
  - Chỉnh file markdown: sửa chỉ dẫn trong file, rồi thử lại, mình không cần viết code
  - Ví dụ: một skill vẽ diagram gần đúng, nhưng style màu khác brand của mình, nên mình sửa dòng mô tả màu trong file rồi gọi lại
  - Trong dự án của bạn, thử chọn cách nào cho repo đã chọn ở Open
- 🎨 Visual hint: NUMBERED layout, 3-col override.

### COMPARE · Where to Install a Skill
- Kicker: Scope
- Title: Cài ở đâu để thử
- On-slide:
  - Dùng chung: skill dùng được ở mọi dự án, ảnh hưởng toàn bộ.
  - Một dự án: skill chỉ dùng trong một folder, dễ gỡ.
- Speaker notes:
  - Phạm vi dự án là mặc định an toàn để thử một skill chưa quen, vì chỉ ảnh hưởng một folder
  - Dùng chung phù hợp khi mình đã tin skill và muốn dùng ở mọi dự án
  - Cách cài và cách gọi khác nhau theo tool. Câu lệnh dùng được ở mọi tool: gửi link repo và nhờ "cài skill này ở phạm vi dự án, cho biết nó nằm ở đâu và gọi nó thế nào"
  - **Kiểm tra (30 giây):** với một skill chưa quen, nên cài dùng chung hay chỉ cho một dự án trước?
  - Ví dụ: một designer cài skill mới ở phạm vi một folder thử, không thích thì xoá folder, không để lại gì
- 🎨 Visual hint: SCHEMATIC. Hai cột, hai vòng tròn: vòng lớn bao nhiều dự án, vòng nhỏ một dự án.

---

## 2. Bridge

### MILESTONE · Break and Check
- Kicker: Bridge
- Num: 5
- Title: Nghỉ và kiểm tra\nnhanh
- Sub: Hai phút nghỉ, hai phút kiểm tra, một phút xem task card.
- Speaker notes:
  - Nghỉ ngắn hai phút
  - Ba câu hỏi miệng: skill khác template repo ở đâu? Kể ba dấu hiệu trên trang repo. Vì sao viết dự đoán trước khi nhờ AI?
  - Cho xem task card và cheat sheet sẽ ở lại trên màn hình suốt Practice
- 🎨 Visual hint: MILESTONE layout, sienna background, num 280px.

### DIAGRAM · Cheat Sheet
- Kicker: Cheat sheet
- Title: Trước khi giữ một repo
- On-slide:
  - Loại gì? Skill, template, component library hay file rules.
  - Ai làm, cập nhật lần cuối khi nào?
  - Có license, cho phép dùng lại không?
  - Dự đoán khớp và lệch với diễn giải của AI ở đâu?
  - Có chỉ dẫn chạy lệnh, xoá file hay gửi dữ liệu ra ngoài không?
  - Đã nhờ AI chấm độ tin cậy, và hiểu giới hạn của điểm chấm chưa?
  - Đang clone vào folder mới, tách khỏi dự án thật chưa?
- Speaker notes:
  - Đây là cheat sheet ở lại trên màn hình suốt Practice, không phải kiến thức mới
  - Mỗi dòng trỏ về một phần Theory: loại, dấu hiệu bên ngoài, diễn giải và chấm điểm bằng AI, folder tách riêng
  - Ví dụ: học viên kẹt ở bước chỉnh, nhìn cheat sheet thấy mình chưa kiểm tra license
  - Nhắc học viên in hoặc chụp cheat sheet nếu muốn dùng lại
- 🎨 Visual hint: SCHEMATIC. Danh sách bảy dòng với ô tick, đọc được từ xa.

---

## 3. Practice

### SECTION DIVIDER · Practice
- Kicker: Practice
- Title: Clone, đọc,\n*chỉnh*
- Sub: Một template repo, một folder mới, một outcome chạy thử.
- Speaker notes:
  - Practice liền mạch, không quay lại dạy giữa chừng
  - Mình đi quanh, hỏi thay vì chỉ cách
  - Nếu nhiều học viên cùng vướng một chỗ thì mới dừng lại giải thích chung
- 🎨 Visual hint: SECTION DIVIDER layout, `--paper-deeper` background.

### MILESTONE · Practice
- Kicker: Practice
- Num: 30
- Title: Clone, đọc và chỉnh\nmột template repo
- Sub: Một folder mới, tách khỏi dự án thật.
- Speaker notes:
  - Học viên chọn template repo mặc định là repo template của Winnie, hoặc repo khác trong handout nếu có license mở
  - Bắt đầu bằng ba dòng dự đoán, chưa mở AI
  - Hỏi những ai kẹt khi cài hoặc clone, hỗ trợ ngay để không mất thời gian
- 🎨 Visual hint: MILESTONE layout, sienna background.

### PROCESS · Task Card
- Kicker: Task
- Title: Năm bước
- On-slide:
  - 1 · Xem trang repo, viết dự đoán ba dòng.
  - 2 · Clone vào folder mới, không dùng folder dự án thật.
  - 3 · Đưa markdown cho AI, đối chiếu với dự đoán.
  - 4 · Nhờ AI đổi tên và ngữ cảnh trong cả repo, rồi mở file kiểm tra.
  - 5 · Chạy thử một outcome, kết thúc bằng một dòng giữ, sửa hay bỏ.
- Speaker notes:
  - Bước 1 khoảng ba phút, bước 2 năm phút, bước 3 tám phút, bước 4 mười phút, bước 5 bốn phút
  - Bước 4: nhờ AI coding tool đổi tên và ngữ cảnh trong toàn repo, nêu rõ tên mới và file cần đổi. Sau đó tự mở các file để kiểm tra, chỉ sửa tay chỗ AI bỏ sót hoặc đổi nhầm, rồi chỉnh thêm một file rules hoặc step card
  - Bước 5 có hai nhánh: với template thì nhờ AI coding tool tạo một dự án mới theo hướng dẫn trong repo, với skill thì cài ở phạm vi dự án trong folder mới rồi gọi thử
  - Điểm hay gặp: bỏ qua dự đoán, hoặc clone vào folder dự án thật, hoặc coi lời AI "an toàn" là kết luận, hoặc chấp nhận kết quả đổi hàng loạt mà không mở file kiểm tra
  - Nếu AI coding tool hỏi quyền chạy lệnh mà học viên chưa hiểu, dừng lại và hỏi AI nó cần quyền đó để làm gì
- 🎨 Visual hint: SCHEMATIC. Process 5 bước ngang, `repeat(5,1fr)`, bước 3 và 4 nhấn sienna.

### IMAGE · The Template Repo
- Kicker: Starting point
- Title: Nút "Use this template"
- On-slide: Repo template mặc định cho Practice, có sẵn demo case và README.
- Speaker notes:
  - Chỉ vào nút "Use this template", thư mục demo-case, my-case và README
  - Ví dụ: một designer clone repo, mở README, đoán đây là workspace dựng quy trình design từ discovery tới deliver
  - Nhắc: repo cần có license `[to confirm]` trước khi dùng cho học viên
  - Trong dự án của bạn, thử đoán repo này giúp việc nào lặp lại
- 🎨 Visual hint: REAL. Ảnh chụp `../assets/lesson-5-template-repo-use-this-template.webp`, giữ nguyên tên trong ảnh.

---

## 4. Bonus

### SECTION DIVIDER · Bonus
- Kicker: Bonus
- Title: Một workflow\ndựng *sẵn*
- Sub: Một template để tự sáng tạo workflow của riêng mình.
- Speaker notes:
  - Giới thiệu sơ qua một workflow mình đã dựng trên repo template, không phải bán hàng
  - Mục đích: học viên thấy repo đó làm được gì, rồi tự sáng tạo workflow của mình từ template
  - Nói rõ đây là cách làm của một người, không có nghiên cứu kiểm chứng đi kèm
- 🎨 Visual hint: SECTION DIVIDER layout, `--paper-deeper` background.

### DIAGRAM · Double Diamond, One Place
- Kicker: The workflow
- Title: Cả quy trình, một nơi
- On-slide: Discovery tới deliver theo Double Diamond. Đầu ra của activity này là đầu vào của activity sau.
- Speaker notes:
  - Vấn đề mình gặp: ba tháng sau có người hỏi "sao mình chọn thế này?", công việc nằm rải rác ở tài liệu, ghi chú, slide và file design
  - Workspace chạy theo Double Diamond, từ discovery problem, competitor research, desk research, user interview tới diagram user flow, service blueprint và prototype
  - Mọi thứ gom về một nơi và một artifact
  - Đầu ra của activity này là đầu vào của activity sau, mọi thứ cross-refer nhau
  - Nhờ vậy thấy được quyết định nào đã đóng, quyết định nào cần tập trung, và giữ nhất quán cho sản phẩm
- 🎨 Visual hint: SCHEMATIC. Dùng `../assets/lesson-5-showcase-double-diamond.svg`.

### IMAGE · Decisions in Context
- Kicker: Example
- Title: Từ card sort tới sitemap
- On-slide: Ví dụ từ demo case: card sort board và IA sitemap.
- Speaker notes:
  - Cho xem hai ảnh từ demo case: card sort board và IA sitemap
  - Chỉ ra rằng sitemap đến từ card sort, không phải tự nghĩ ra, đây là cross-refer
  - Ví dụ: một quyết định đặt tên menu có lý do và bằng chứng đi kèm, không chỉ là cảm giác
  - Trong dự án của bạn, quyết định nào đang thiếu bằng chứng?
- 🎨 Visual hint: REAL. Hai ảnh cạnh nhau: `../assets/lesson-5-showcase-card-sort-board.png` và `../assets/lesson-5-showcase-ia-sitemap.png`.

### IMAGE · Screens From the Demo Case
- Kicker: Example
- Title: Năm màn hình wireframe
- On-slide: Năm màn hình từ demo case, dựng từ cùng workflow.
- Speaker notes:
  - Năm màn hình onboarding, discover, plan, connect và journal đến từ cùng workspace
  - Mỗi màn hình dẫn ngược về user need và quyết định đứng sau nó
  - Nguyên tắc: AI soạn nháp có dẫn nguồn, designer quyết định
  - Không có con số hiệu quả nào để nói, vì đây là cách làm của một người
- 🎨 Visual hint: REAL. Năm ảnh `../assets/lesson-5-showcase-wireframe-1-onboarding.png` đến `...-5-journal.png` xếp một hàng.

### FORMULA · Make It Yours
- Kicker: Reuse it
- Title: Từ template đến workflow của bạn
- On-slide:
  - Bấm "Use this template"
  - Thay nội dung bằng dự án của mình
  - Sửa các file markdown và step card thành workflow riêng
- Speaker notes:
  - Mỗi dòng nặng hơn dòng trước: dùng template, thay nội dung, rồi chỉnh quy trình
  - Dòng cuối là hành động: sửa file markdown và step card để workflow mô tả đúng cách mình làm
  - Đây cũng là chính repo vừa dùng ở Practice, nên không cần học thêm gì mới
  - Ví dụ: một designer thêm một step card cho bước phỏng vấn mà quy trình mặc định chưa có
- 🎨 Visual hint: TYPOGRAPHIC. Ba dòng tăng dần: `--ink` → `--ochre` → `--sienna`.

---

## 5. Close

### PRACTICE · Homework
- Kicker: Homework
- Title: Một việc, ba ứng viên
- On-slide:
  - Chọn một việc lặp lại trong dự án đang làm.
  - Tìm ba ứng viên từ hai nguồn, chấm theo cheat sheet.
  - Thử một ứng viên trong folder mới, viết giữ, sửa hay bỏ kèm lý do.
- Speaker notes:
  - Mỗi học viên nêu quyết định cho repo vừa thử trong một câu: giữ nguyên, sửa hay bỏ, và vì sao
  - Giao bài tập: chọn một việc chưa có skill hoặc template, tìm ba ứng viên từ hai nguồn, chấm theo cheat sheet
  - Nhắc handout danh sách skill để học viên đào thêm
  - Thời hạn và cách nộp `[to confirm]`
- 🎨 Visual hint: PRACTICE layout, hai card, tiêu đề 52px, bullet mũi tên sienna.

### END · Thank You
- Kicker: Lesson 5
- Title: *Reuse*
- Sign: Winnie Nguyen
- Contact: Handout nằm trong bộ tài liệu của lesson.
- Speaker notes:
  - Kết bằng một câu: dùng lại không phải đi đường tắt, mà là biết chọn, đọc và thử trước khi tin
  - Nhắc handout để học viên đào thêm sau buổi học
  - Nhắc một điều trước khi về: trong công ty, hỏi chính sách trước khi nối skill hoặc repo bên ngoài vào repo của công ty. Phần thử nên làm ở repo cá nhân với dữ liệu mẫu
  - Hỏi nhanh có câu hỏi nào còn lại
- 🎨 Visual hint: END layout, `--paper-deeper` background.

---

## Drift to resolve

Deck được build ngày 2026-10-18, sau khi outline và lesson được cập nhật ngày 2026-10-17 (WF-2). Nội dung mới có vẻ chưa có trong deck `[to confirm]` bằng cách mở deck:

- **Task Card bước 4:** deck còn ghi "Đổi tên, ngữ cảnh và file rules thành của bạn". Outline và lesson đã đổi thành nhờ AI đổi hàng loạt rồi mở file kiểm tra.
- **Bước nhờ AI chấm độ tin cậy và an toàn:** slide Read Without Reading Code và dòng thứ bảy của Cheat Sheet chưa thấy trong deck.
- **Ghi chú môi trường doanh nghiệp:** hỏi chính sách trước khi nối skill hoặc repo bên ngoài vào repo của công ty, chưa thấy ở slide kết.
- **Số slide:** outline ghi 25 slide, cần đếm lại trong deck để đối chiếu.

Cập nhật deck cho khớp, hoặc giữ các điểm này như lời nói. Khi hai bên khác nhau, file lesson là nguồn đúng.
