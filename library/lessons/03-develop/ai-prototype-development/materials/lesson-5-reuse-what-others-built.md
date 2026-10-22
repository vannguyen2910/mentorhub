---
title: "Systematic AI Prototyping — Lesson 5: Reuse What Others Built"
subtitle: "Tìm, đọc và dùng lại skill hoặc repo của người khác mà không cần đọc code"
type: lesson
program: private-training
stage: Develop
tags: [ai-in-ux, prototyping, design-systems, private-training, intermediate]
level: intermediate
duration: "90 min"
date: 2026-10-17
draft: true
slides: "../slides/Lesson 5 - Reuse What Others Built.dc.html"
previous-session: "Lesson 4: Publish It"
next-session: "None (bài extra bonus cuối arc)"
---

> **Bài extra bonus**, nằm sau Lesson 4 trong arc private-training, dành cho designer không code. Brief đã được duyệt ngày 2026-10-17 (`lesson-5-reuse-what-others-built-brief.md`). Slide outline ghép đôi: `lesson-5-slide-outline.md`. Handout danh sách skill: `../assets/lesson-5-skills-handout.md`.

---

## Overview

Nhiều việc designer làm lặp lại đã có người dựng sẵn thành skill hoặc template repo công khai trên GitHub. Một designer thấy các creator trên TikTok và YouTube dùng một skill vẽ diagram có styling và complex diagram, vào repo công khai của skill đó, đọc README, nhờ AI coding tool cài vào, rồi về sau gọi skill bằng tên trong các task cần vẽ diagram. Quy trình này không cần đọc code, nhưng cần biết tìm ở đâu, đọc gì trước khi cài, và cài vào đâu để thử.

Bài học trình bày quy trình đó cho designer không code: phân biệt các loại thứ dùng lại được, tìm trên GitHub và awesome list, đọc một repo qua trang GitHub và file markdown được AI diễn giải, clone vào folder mới tách khỏi dự án thật, rồi chỉnh thành đầu ra của mình. Phần Practice dùng một template repo. Phần Bonus giới thiệu một workflow dựng sẵn trên template repo của Winnie như một ví dụ về việc tự sáng tạo workflow từ một template.

**Giới hạn đã nêu ngay từ đầu:** AI diễn giải file markdown chỉ là một lớp kiểm tra và không bảo đảm repo an toàn (xem Limitations).

---

## Learning Objectives

Sau buổi học, học viên có thể:

1. **Phân biệt** skill, template repo, component library và file rules, rồi chọn đúng loại cho một nhu cầu cụ thể.
2. **Tìm** ít nhất ba ứng viên từ hai nguồn (GitHub search, awesome list).
3. **Đánh giá** một repo qua trang GitHub của nó (README, số sao, lần cập nhật cuối, license) và nhờ AI chấm độ tin cậy, an toàn, kèm nêu được giới hạn của điểm chấm đó.
4. **Diễn giải** một repo bằng cách đưa các file markdown cho AI chat tool, và nêu được những gì AI không xác nhận được.
5. **Clone** một template repo vào folder mới và **chỉnh** nó thành đầu ra cho dự án của chính mình, bằng cách nhờ AI đổi ngữ cảnh rồi tự kiểm tra kết quả.

Phần Bonus nằm ngoài các mục tiêu được đánh giá.

---

## Success Check

Cuối buổi, học viên có:

- Một folder mới đã clone từ một template repo, tách khỏi dự án thật.
- Ba dòng dự đoán viết trước khi mở AI, kèm ghi chú những chỗ AI diễn giải khác dự đoán.
- Một outcome đã chạy thử trên nội dung của chính học viên.
- Một quyết định bằng lời cho repo đó: giữ nguyên, sửa hay bỏ, kèm lý do.

---

## Materials Needed

- GitHub Desktop đã cài và đã đăng nhập (từ Lesson 4).
- Một AI chat tool và một AI coding tool của học viên.
- Cheat sheet một trang (slide Bridge, cũng in ra được).
- Handout danh sách skill và repo (`../assets/lesson-5-skills-handout.md`).
- Ảnh trong `../assets/`: trang repo (số sao, license, commit gần nhất), template repo có nút "Use this template", trang GitHub Marketplace, và một user flow swimlane do diagram skill dựng (`lesson-5-showcase-user-flow-swimlane.webp`).
- Template repo của Winnie `[to confirm]` đã có license và README đủ rõ.

---

## Pre-Class Preparation

- Học viên chọn trước một việc đã làm lặp lại trong dự án (ví dụ vẽ diagram, tổng hợp phỏng vấn, viết spec cho dev) để dùng ở phần Open.
- Học viên tạo một folder trống làm nơi clone, nằm tách khỏi folder dự án thật.

---

## Run-of-Show

Tổng 85 phút cộng 5 phút đệm. Theo thứ tự theory trước, practice sau (Rule LP-3).

| Giờ | Block | Phút |
|---|---|---|
| 00:00 | Open | 5 |
| 00:05 | Theory (4 phần) | 30 |
| 00:35 | Bridge | 5 |
| 00:40 | Practice | 30 |
| 01:10 | Bonus | 10 |
| 01:20 | Close | 5 |
| 01:25 | Đệm | 5 |

**Phần có thể co lại khi quá giờ:** Bonus rút còn 5 phút (giữ ba ảnh và câu "dùng làm template"). Theory (b) rút còn 5 phút nếu học viên đã quen tìm trên GitHub.

### [00:00] Open (5 phút)

Câu chuyện mở: một designer cần vẽ diagram có styling và complex diagram, thấy các creator trên mạng xã hội dùng một skill làm được điều đó. Designer tìm ra repo công khai của skill, đọc README, nhờ AI coding tool cài vào ở phạm vi dùng chung cho mọi dự án (hoặc chỉ cho một dự án), rồi về sau gọi skill bằng tên khi cần. Kết quả thật của skill đó (một user flow dạng swimlane từ demo case) được chiếu ngay sau câu chuyện để học viên thấy đầu ra cụ thể. Câu hỏi chuyển: dự án của học viên có việc nào lặp lại mà có thể đã có người làm rồi?

---

### [00:05] Theory (30 phút)

#### Part 1 — Bốn thứ dùng lại được (5 phút)

| Loại | Là gì | Ví dụ việc cần |
|---|---|---|
| Skill | Folder có file `SKILL.md` gồm tên, mô tả và hướng dẫn. AI coding tool đọc và làm theo khi được gọi | Vẽ diagram theo một style cố định |
| Template repo | Repo mẫu có folder, file markdown và quy trình dựng sẵn. Dùng bằng nút "Use this template" hoặc clone | Workspace cho cả một quy trình design |
| Component library | Bộ component chép vào dự án | Bộ nút, form, bảng |
| File rules | Một hai file markdown chứa luật cho AI tool | Luật đặt tên, giọng văn, cấu trúc folder |

Skill là một folder có file `SKILL.md`, gồm phần đầu (tên và mô tả) và phần hướng dẫn bằng markdown, kèm script và tài liệu nếu cần [1][2]. Phần lớn nội dung của skill, template và file rules là markdown, nên học viên đọc và chỉnh được mà không cần viết code.

**Check (30 giây).** Với việc lặp lại học viên chọn ở Open, loại nào phù hợp nhất?

#### Part 2 — Tìm ở đâu và đọc trang repo (10 phút)

Nguồn tìm trong bài: GitHub search, awesome list và trang riêng của từng tool. GitHub Marketplace trong ảnh chụp chỉ liệt kê Apps và Actions, không có mục skill, nên không dùng làm nguồn tìm skill `[to confirm]`. Awesome list là danh sách tuyển chọn trên GitHub, đã được người duy trì lọc một lần [6]. Mạng xã hội thường là nơi học viên bắt gặp một skill lần đầu. Khi đó cần lần ra repo gốc thay vì cài từ link của bài đăng.

Trang repo cho sẵn các dấu hiệu bên ngoài, đọc được mà không cần mở code:

| Dấu hiệu | Ở đâu trên trang | Cho biết |
|---|---|---|
| Tác giả và tổ chức | Đầu trang | Ai đứng sau |
| Số sao, fork, watching | Cột bên phải và nút trên cùng | Mức độ được quan tâm |
| Commit gần nhất | Dòng phía trên danh sách file | Repo còn được bảo trì không |
| License | Cột About | Được phép dùng lại và sửa không |
| README | Phần dưới danh sách file | Repo làm gì và dùng thế nào |

Số sao cao là tín hiệu quan tâm, không phải bằng chứng an toàn. Các danh sách tổng hợp của các hãng bảo mật cũng cho thấy skill bị tải xuống nhiều vẫn có thể có vấn đề (xem Background).

**Check (30 giây).** Một repo có 200 sao nhưng commit cuối cách đây hai năm và không có license. Dấu hiệu nào đáng lo nhất?

#### Part 3 — Đọc mà không cần đọc code (10 phút)

Học viên không đọc code, nên bước kiểm tra dựa trên file markdown: đưa README và các file `.md` chính (hướng dẫn, `SKILL.md`, `AGENTS.md`) cho AI chat tool, và hỏi bằng lời thường:

- Repo này làm gì, cho ai, đầu ra là gì?
- Mỗi file markdown chỉ dẫn AI làm gì?
- Có chỉ dẫn nào yêu cầu chạy lệnh, xoá hoặc ghi đè file, đọc file ngoài folder này, hoặc gửi dữ liệu ra ngoài không?
- Những điểm nào AI không chắc?

Thứ tự bắt buộc: học viên tự xem README, ảnh và mô tả rồi viết dự đoán ba dòng trước, sau đó mới nhờ AI diễn giải để đối chiếu. Làm ngược lại thì dự đoán bị AI định hướng, và học viên khó nhận ra chỗ AI diễn giải khác thực tế.

Sau bước diễn giải, học viên nhờ AI chat tool chấm độ tin cậy và an toàn của repo theo một bộ câu hỏi cố định: nguồn và tác giả, lần cập nhật cuối, license, cách chạy lệnh, quyền cần có, chỉ dẫn gửi dữ liệu ra ngoài. Điểm chấm chỉ là ý kiến tham khảo. AI chấm dựa trên chính những file nó được đọc, nên không thay được các dấu hiệu bên ngoài ở Part 2 và không loại trừ chỉ dẫn độc hại nằm trong file [4]. Phần này chiếm khoảng 2 phút và lấy từ phần đệm của buổi. Bộ câu hỏi chấm do người dạy viết hay lấy từ nguồn ngoài `[to confirm]`.

**Check (30 giây).** AI nói "repo này an toàn". Câu trả lời đó nên được hiểu thế nào?

#### Part 4 — Ba cách dùng lại và phạm vi cài (5 phút)

| Cách | Khi nào | Việc cần làm |
|---|---|---|
| Dùng nguyên bản | Repo làm đúng việc cần | Clone hoặc cài, rồi dùng |
| Lấy làm template | Cấu trúc đúng, nội dung khác | Thay nội dung bằng của mình |
| Chỉnh file markdown | Gần đúng, cần khác ở vài chỗ | Sửa chỉ dẫn trong file, rồi thử lại |

Với skill còn một lựa chọn nữa: cài dùng chung cho mọi dự án, hoặc chỉ cho một dự án. Cách cài và cách gọi skill khác nhau theo từng tool, nên lesson giữ chung. Câu lệnh dùng được ở mọi tool: gửi link repo cho AI coding tool và nhờ "cài skill này ở phạm vi dự án, cho biết nó nằm ở đâu và gọi nó thế nào" `[to confirm]` mỗi tool trả lời đúng cách thức riêng của nó. Phạm vi dự án là mặc định an toàn để thử, vì skill chỉ ảnh hưởng một folder.

**Check (30 giây).** Với một skill chưa quen, nên cài dùng chung hay chỉ cho một dự án trước?

---

### [00:35] Bridge (5 phút)

1. **Nghỉ ngắn (2 phút).**
2. **Kiểm tra nhanh (2 phút).** Ba câu hỏi miệng lấy từ phần Assessment.
3. **Task card (1 phút).** Các bước Practice, thời gian từng bước và cheat sheet.

**Cheat sheet (một màn hình, ở lại suốt Practice):**

| Trước khi giữ một repo, cần trả lời |
|---|
| Loại gì? (skill, template, component library, file rules) |
| Ai làm, lần cập nhật cuối khi nào? |
| Có license chưa, cho phép dùng lại không? |
| Dự đoán của mình khớp với diễn giải của AI ở chỗ nào, lệch ở chỗ nào? |
| Có chỉ dẫn nào về chạy lệnh, xoá file hoặc gửi dữ liệu ra ngoài không? |
| Đã nhờ AI chấm độ tin cậy và an toàn chưa, và đã hiểu giới hạn của điểm chấm đó chưa? |
| Đang clone vào folder mới, tách khỏi dự án thật chưa? |

---

### [00:40] Practice (30 phút, liền mạch)

**Setup:** học viên mở GitHub Desktop, folder trống đã chuẩn bị, AI chat tool và AI coding tool. Template repo mặc định là repo template của Winnie. Học viên cũng có thể chọn một repo khác từ handout nếu repo đó có license mở.

**Task:**

1. **Chọn và dự đoán (3 phút).** Xem trang repo, đọc các dấu hiệu bên ngoài trên cheat sheet, rồi viết ba dòng: repo làm gì, cho ai, đầu ra là gì.
2. **Clone vào folder mới (5 phút).** Dùng GitHub Desktop để clone vào folder trống đã chuẩn bị, không clone vào folder dự án thật.
3. **Đưa markdown cho AI (8 phút).** Dùng prompt ở phần AI in Practice, đối chiếu với dự đoán, ghi những chỗ khác nhau và những chỗ AI không chắc.
4. **Chỉnh theo dự án của mình (10 phút).** Nhờ AI coding tool đổi tên dự án và ngữ cảnh trong toàn repo thành của mình, nêu rõ tên mới và những file cần đổi. Sau đó học viên mở các file đã đổi để kiểm tra, chỉ sửa tay những chỗ AI bỏ sót hoặc đổi nhầm, rồi chỉnh thêm một file rules hoặc step card. Lý do không sửa tay từng file: repo template có nhiều file nên sửa tay dễ sót.
5. **Chạy thử một outcome (4 phút).** Hai nhánh tuỳ repo đã chọn: với template, nhờ AI coding tool tạo một dự án mới theo hướng dẫn trong repo và xem kết quả; với skill, nhờ AI coding tool cài skill ở phạm vi dự án trong folder mới, rồi gọi thử một lần. Kết thúc bằng một dòng: giữ, sửa hay bỏ, và vì sao.

**Điểm cần quan sát (cho người dạy):**

- Học viên bỏ qua bước viết dự đoán và mở AI ngay: dự đoán là phần bắt buộc, vì không có nó thì không đối chiếu được.
- Học viên clone vào folder dự án thật: cần chuyển sang folder mới trước khi tiếp tục.
- Học viên coi diễn giải hoặc điểm chấm của AI là kết luận về độ an toàn: nhắc lại ghi chú về giới hạn ở Limitations.
- Học viên chấp nhận kết quả đổi hàng loạt mà không mở file kiểm tra: nhắc rằng AI có thể đổi sót hoặc đổi nhầm.
- AI coding tool hỏi quyền cài hoặc quyền chạy lệnh mà học viên chưa hiểu: học viên hỏi lại AI quyền đó dùng để làm gì trước khi đồng ý.

---

### [01:10] Bonus (10 phút): một workflow dựng sẵn trên repo template

Giới thiệu sơ qua một workflow đã dựng sẵn trên repo template của Winnie, để học viên thấy repo đó làm được gì và có thể dùng làm template để tự sáng tạo workflow của riêng mình. Đây là cách làm của một người, không có nghiên cứu kiểm chứng đi kèm.

- **Vấn đề:** ba tháng sau có người hỏi "sao mình chọn thế này?", công việc nằm rải rác ở tài liệu, ghi chú, slide và file design.
- **Cách làm:** workspace theo Double Diamond, từ discovery (discovery problem, competitor research, desk research, user interview) tới deliver (diagram user flow, service blueprint, prototype), gom về một nơi và một artifact.
- **Điểm cốt lõi:** đầu ra của activity này là đầu vào của activity sau, mọi thứ cross-refer nhau, nên thấy được quyết định nào đã đóng, quyết định nào cần tập trung, và giữ được tính nhất quán cho sản phẩm.
- **Nguyên tắc:** AI soạn nháp có dẫn nguồn, designer quyết định.
- **Cách dùng lại:** bấm "Use this template", thay nội dung bằng dự án của mình, rồi sửa các file markdown và step card để thành workflow riêng.

Ảnh dùng từ demo case của repo (`../assets/lesson-5-showcase-*`): double diamond, sitemap, card sort board và năm màn hình wireframe.

---

### [01:20] Close (5 phút)

Mỗi học viên nêu một quyết định cho repo đã thử (giữ nguyên, sửa hay bỏ) và lý do trong một câu. Giao bài tập (xem Assessment). Handout danh sách skill để học viên tự tìm hiểu thêm. Lời nhắc cuối: trong môi trường doanh nghiệp, nên hỏi chính sách trước khi nối skill hoặc repo bên ngoài vào repo của công ty; phần thử nên làm ở repo cá nhân với dữ liệu mẫu (xem Limitations).

---

## AI in Practice

### 🤖 Try this with AI

> Prompt dùng trong AI chat tool, kèm nội dung README và các file markdown chính của repo:
> *"Đây là README và các file markdown của một repo trên GitHub. Hãy giải thích bằng lời thường cho một designer không biết code: repo này làm gì, dành cho ai, đầu ra là gì, gồm những thư mục nào, và mỗi file markdown chỉ dẫn AI làm gì. Sau đó liệt kê mọi chỉ dẫn yêu cầu chạy lệnh, xoá hoặc ghi đè file, đọc file ngoài folder này, hoặc gửi dữ liệu ra ngoài. Cuối cùng liệt kê những điểm bạn không chắc."*

Prompt thứ hai, dùng ngay sau prompt trên:
> *"Dựa trên các file này, hãy chấm độ tin cậy và độ an toàn của repo theo từng tiêu chí: nguồn và tác giả, lần cập nhật cuối, license, cách chạy lệnh, quyền cần có, chỉ dẫn gửi dữ liệu ra ngoài. Với mỗi tiêu chí, trích đoạn file làm căn cứ và nói rõ phần nào bạn không thể kiểm tra từ những file này."*

Trong bộ prompt này, tên tiêu chí được viết sẵn để học viên đối chiếu với cheat sheet. Điểm chấm là ý kiến tham khảo của AI, không phải kết luận về độ an toàn.

### 🧠 Critical thinking prompt

- AI diễn giải khớp với dự đoán ở chỗ nào, lệch ở chỗ nào?
- AI nói chung chung hoặc bỏ qua điều gì? Nó có nêu điểm không chắc không?
- AI không có thông tin gì về dự án của học viên mà vẫn đưa ra nhận định?
- Có chỉ dẫn nào trong file mà AI không nhắc tới?
- Điểm chấm của AI dựa trên căn cứ nào, và có tiêu chí nào AI chấm mà không có căn cứ trong file?

### ✍️ Prompt engineering tip

Yêu cầu AI tách rõ "điều có trong file" và "điều suy đoán". Prompt có thêm câu "đánh dấu phần nào bạn suy đoán" giúp học viên thấy chỗ diễn giải không có căn cứ trong file.

### ⚖️ Ethics consideration

Dùng lại công việc của người khác có điều kiện đi kèm. License quyết định được dùng lại, sửa và chia sẻ lại ở mức nào, và repo không có license mặc định là chưa cho phép dùng lại. Khi dùng lại hoặc sửa, nên ghi nguồn tác giả. Không đưa key, token hay dữ liệu khách hàng thật vào folder vừa clone.

---

## Assessment

### Quick knowledge check

1. Skill khác template repo ở điểm nào?
2. Kể ba dấu hiệu bên ngoài trên trang repo cần xem trước khi cài.
3. Vì sao dự đoán được viết trước khi nhờ AI diễn giải?
4. Một skill chưa quen nên cài ở phạm vi nào trước, và vì sao?

### Reflection prompt (homework)

> *"Chọn một việc trong dự án đang làm mà chưa có skill hoặc template. Tìm ba ứng viên từ hai nguồn, chấm theo cheat sheet, chọn một, thử trong folder mới và viết quyết định giữ, sửa hay bỏ kèm lý do."*

Thời hạn và cách nộp `[to confirm]`.

---

## Background

**Phát hiện từ nguồn.** Ba nghiên cứu của các hãng bảo mật và nhóm nghiên cứu cho thấy skill của người khác có rủi ro đáng kể (số liệu tóm tắt qua các bài tổng hợp, `[to confirm]` bằng báo cáo gốc trước khi dùng trên slide):

- "Agent Skills in the Wild" phân tích 31.132 skill thu từ hai marketplace lớn, và thấy 26,1% có ít nhất một lỗ hổng thuộc bốn nhóm: prompt injection, rò rỉ dữ liệu, leo thang quyền và rủi ro chuỗi cung ứng [3].
- Báo cáo ToxicSkills của Snyk quét gần 4.000 skill và ghi nhận 13,4% có vấn đề nghiêm trọng, trong đó 76 skill có payload độc hại được xác nhận [4].
- ESET (nửa đầu 2026) phân tích khoảng 900.000 skill, gắn cờ khoảng 25.000 skill đáng ngờ và hơn 3.000 skill độc hại trực tiếp. ESET cảnh báo chỉ dẫn độc hại có thể nằm ngay trong README và các tài liệu mà AI đọc [4].
- Khuyến nghị chung của các nguồn: coi mỗi lần cài skill như chạy code chưa được review [5].

Các số liệu không so sánh trực tiếp được vì phương pháp và mẫu khác nhau, và phần lớn đến từ nghiên cứu của các hãng bảo mật.

**Suy luận của tác giả.** Với designer không đọc được code, các lớp bảo vệ dựa trên con người (đọc code) không dùng được. Lesson đề xuất kết hợp ba lớp không cần đọc code: dấu hiệu bên ngoài, diễn giải markdown bằng AI, và clone vào folder tách khỏi dự án thật. Đây là cách làm của Winnie, không có nghiên cứu kiểm chứng riêng.

---

## Limitations

- AI diễn giải file markdown không bảo đảm file an toàn: chỉ dẫn độc hại có thể ẩn trong chính README mà AI đọc [4], và AI có thể bỏ sót hoặc diễn giải sai. Bước này là một lớp kiểm tra, không phải lớp duy nhất.
- Học viên không đọc được code, nên chỉ nên dùng repo có số sao và lần cập nhật hợp lý, có license, và không đưa key hay file thật vào folder vừa clone.
- Các số liệu bảo mật ở Background đến từ các bài tổng hợp, chưa được đối chiếu với báo cáo gốc. Danh sách skill trong handout đến từ các bài tổng hợp và kết quả tìm kiếm, chưa kiểm tra từng repo (số sao, license, lần cập nhật).
- Cách cài và gọi skill khác nhau theo tool. Bài chỉ trình bày chung, và học viên cần kiểm tra cách thức của tool mình dùng.
- Điểm chấm độ tin cậy do AI đưa ra dựa trên chính các file nó đọc, nên không phát hiện được chỉ dẫn độc hại nằm trong những file đó [4]. Điểm chấm chỉ dùng cùng các dấu hiệu bên ngoài, không dùng thay chúng.
- Trong môi trường doanh nghiệp, skill và repo bên ngoài thường không được phép nối vào repo của công ty, và nhiều công ty tự dựng skill, agent và template nội bộ. Đây là quan sát của người dạy, không có nghiên cứu kèm theo `[to confirm]`. Bài hướng dẫn thử ở repo cá nhân với dữ liệu mẫu, và học viên cần theo chính sách của nơi mình làm việc.

---

## Further Resources

Handout đầy đủ (kèm ghi chú và `[to confirm]`) ở `../assets/lesson-5-skills-handout.md`. Tóm tắt theo nhu cầu:

**User flow, diagram:** diagram-design (cathrynlavery), customer-journey-map (aiuxplayground).
**User research:** uh-joan/ux-research-skills, miguelclavel/ux-research-skills, SkillMedev/ux-research-discovery, LTraina0/design-skills.
**Journey mapping, service blueprint:** cguodesign/customer-journey-map-skill, rampstackco/claude-skills (journey-mapping), deanpeters/Product-Manager-Skills (customer-journey-map), GeorgeQLe service-blueprint.
**Hand off cho developer:** design-handoff (anthropics/knowledge-work-plugins), Owl-Listener/designer-skills, plugin87/ux-ui-agent-skills.
**Product management:** phuryn/pm-skills, product-on-purpose/pm-skills, deanpeters/Product-Manager-Skills.
**Design (UI/UX):** frontend-design (anthropics), Impeccable (pbakaus), UI UX Pro Max (nextlevelbuilder), Interface Design (dammyjay93), Vercel Web Design Guidelines.

---

## References

1. Parallel. "What are agent skills? SKILL.md and the portable-capability standard." parallel.ai/articles/what-are-agent-skills.md (2026).
2. Firecrawl. "Agent Skills." firecrawl.dev/blog/agent-skills (2026).
3. Forkast. "AI agent skills are the new supply chain attack vector and most have never been vetted." Tóm tắt nghiên cứu "Agent Skills in the Wild" (31.132 skill được phân tích). forkast.news (2026). `[to confirm]` bằng nghiên cứu gốc.
4. Expert Insights. "1 in 300 AI agent skills is directly malicious, ESET research finds." Gồm tóm tắt ESET H1 2026 và Snyk ToxicSkills. expertinsights.com (2026). `[to confirm]` bằng báo cáo gốc.
5. SafeDep. "Agent Skills Threat Model." safedep.io/agent-skills-threat-model (2026).
6. birobirobiro. "awesome-shadcn-ui." github.com/birobirobiro/awesome-shadcn-ui, license MIT (kiểm tra license từng repo trước khi dùng lại).

---

*Created by Winnie Nguyen · Private Training · Last updated October 2026*
