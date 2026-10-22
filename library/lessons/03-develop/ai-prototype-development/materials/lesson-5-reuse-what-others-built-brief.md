---
title: "Lesson 5: Reuse What Others Built"
type: lesson
audience: private-training
level: intermediate
duration: "90 min"
---

> **Đã duyệt và build 2026-10-17.** Lesson: `lesson-5-reuse-what-others-built.md`, outline: `lesson-5-slide-outline.md`, handout: `../assets/lesson-5-skills-handout.md`.
>
> **Cập nhật 2026-10-17 (WF-2):** thêm bước nhờ AI chấm độ tin cậy và an toàn (Theory Part 3, cheat sheet, AI in Practice), nhờ AI đổi ngữ cảnh hàng loạt ở Practice bước 4, và ghi chú về môi trường doanh nghiệp ở Limitations và Close. Thời lượng và số slide không đổi.
>
> Bài extra bonus, nằm sau Lesson 4 "Publish It" trong arc private-training. Học viên là designer không code. Tên và slug đã được Winnie chốt ngày 2026-10-17.

## Purpose
Sau buổi học, học viên tìm được một template repo hoặc skill của người khác trên GitHub, clone về, nhờ AI chat tool diễn giải file markdown của nó bằng lời thường, rồi chỉnh theo dự án của mình.

## Structure (85 phút, đệm 5 phút)
1. Open, 5 phút: một câu chuyện thật về việc dùng lại. Một designer thấy trên mạng xã hội (TikTok, YouTube) các creator dùng một skill vẽ diagram có styling và complex diagram, rồi tìm ra repo công khai, đọc README, nhờ AI coding tool cài vào, và về sau gọi skill đó bằng slash command. Kết thúc bằng câu hỏi "có ai làm rồi chưa?" cho dự án của học viên.
2. Theory, 30 phút:
   - (a) 5 phút: bốn thứ dùng lại được, gồm skill, template repo, component library, file rules.
   - (b) 10 phút: tìm ở đâu, gồm GitHub search, marketplace và awesome list. Đọc trang repo: README, số sao, lần cập nhật cuối, license.
   - (c) 10 phút: đọc mà không cần đọc code. Feed README và các file markdown cho AI chat tool, hỏi nó làm gì, đụng vào file nào, cần quyền gì.
   - (d) 5 phút: ba cách dùng lại là dùng nguyên bản, lấy làm template, hoặc chỉnh file markdown theo outcome mình muốn. Skill cài được ở hai phạm vi: dùng chung cho mọi dự án, hoặc chỉ cho một dự án.
3. Bridge, 5 phút: cheat sheet một trang, gồm các câu hỏi cần có câu trả lời trước khi giữ một repo.
4. Practice, 30 phút, liền mạch: chọn một template repo, tự viết dự đoán nó làm gì, clone bằng GitHub Desktop, feed markdown cho AI để đối chiếu, chỉnh nội dung theo dự án của mình, chạy thử một outcome.
5. Bonus, 10 phút, nằm trong 90 phút: giới thiệu sơ qua một workflow dựng sẵn trên repo template của Winnie, để học viên thấy repo đó làm được gì và có thể tự sáng tạo workflow của riêng mình từ một template (xem mục Bonus).
6. Close, 5 phút: mỗi người nêu một quyết định (giữ, sửa hay bỏ) và lý do. Giao bài tập.

## Learning objectives
1. Phân biệt được skill, template repo, component library và file rules, rồi chọn đúng loại cho một nhu cầu cụ thể.
2. Tìm được ít nhất ba ứng viên từ hai nguồn (GitHub search, awesome list).
3. Đánh giá được một repo qua trang GitHub của nó: README, sao, lần cập nhật cuối, license.
4. Diễn giải được repo bằng cách feed file markdown cho AI chat tool, và nêu được những gì AI không xác nhận được.
5. Clone một template repo và chỉnh nó thành đầu ra cho dự án của chính mình.

## Bonus: một workflow dựng sẵn trên repo template (10 phút, trong 90 phút)
Mục đích: cho học viên thấy repo template này làm được gì, và rằng họ có thể dùng nó như một template để tự sáng tạo workflow của mình. Giọng giới thiệu sơ qua, không marketing: không giá, không hạn đăng ký, không con số hiệu quả.

Nội dung, kể theo trải nghiệm của Winnie:
- Vấn đề: ba tháng sau có người hỏi "sao mình chọn thế này?", công việc nằm rải rác ở tài liệu, ghi chú, slide, file design.
- Cách làm: một workspace chạy theo Double Diamond, từ discovery (discovery problem, competitor research, desk research, user interview) tới deliver (diagram user flow, service blueprint, prototype), gom về một nơi và một artifact.
- Điểm cốt lõi: đầu ra của activity này là đầu vào của activity sau, mọi thứ cross-refer nhau, nên thấy được quyết định nào đã đóng, quyết định nào cần tập trung, và giữ được tính nhất quán cho sản phẩm.
- Nguyên tắc: AI soạn nháp có dẫn nguồn, designer quyết định.
- Cách dùng lại: bấm Use this template, thay nội dung bằng dự án của mình, rồi sửa các file markdown và step card để thành workflow riêng. Đây cũng là chính repo dùng cho Practice.
- Kết: không có call to action bán hàng. Nếu cần, một dòng nhắc rằng repo là phần nền của chương trình AI Design Workflow `[to confirm]` có nhắc hay không.

Ảnh dùng (đã lưu trong `../assets/`, lấy từ demo case của repo):
`lesson-5-showcase-double-diamond.svg`, `lesson-5-showcase-ia-sitemap.png`, `lesson-5-showcase-card-sort-board.png`, `lesson-5-showcase-wireframe-1-onboarding.png` đến `...-5-journal.png`, và ảnh trang repo `lesson-5-template-repo-use-this-template.webp`.

Nguồn: README và AGENTS.md của `programs/ai-design-workflow/workspace-template/`, demo case "Travel Buddy" trong repo. Mô tả workflow là cách làm của Winnie, không có nghiên cứu hỗ trợ.

## Key decisions
- Running example: clone một template repo, vì đã có GitHub Desktop từ Lesson 4. Skill được dạy bằng câu chuyện ở Open và Theory (c), (d), không có phần Practice riêng. Lesson dùng nhãn "diagram skill", "workflow skill", "AI coding tool", không ghi tên tool hay tên repo.
- Cài và gọi skill: lesson và slide giữ generic, không ghi tên tool, vì cách cài và cách gọi khác nhau theo tool. Câu lệnh dạy cho học viên không phụ thuộc tool: gửi link repo cho AI coding tool và nhờ "cài skill này, cho biết nó nằm ở đâu và gọi nó thế nào". Winnie demo trực tiếp trên tool của mình, học viên làm lại trên tool của họ. Ví dụ theo từng tool, nếu cần, để ở handout riêng ngoài lesson `[to confirm]`.
- Manual before AI: học viên tự xem README, ảnh và mô tả rồi viết dự đoán trước, sau đó mới nhờ AI diễn giải để đối chiếu.
- Kiểm tra không cần đọc code: feed file markdown cho AI chat tool để diễn giải (Winnie đã chọn).
- Cắt: tự viết skill từ đầu, MCP server.
- Hoãn: dạy làm việc nhóm và pull request vào repo người khác (mục mở số 3 của Lesson 4).
- Nguồn tìm: GitHub search, marketplace và awesome list. Mạng xã hội xuất hiện trong câu chuyện Open như cách học viên có thể bắt gặp một skill, không dạy làm nguồn chính thức. Phần "lần ra repo gốc" nằm trong Theory (b).
- Bonus nằm trong 90 phút, ngay sau Practice để không ngắt Practice.

## Open questions for Winnie
1. ~~Bonus nằm ở đâu~~ Đã chốt: trong 90 phút.
2. ~~Giọng marketing~~ Đã chốt: giới thiệu sơ qua, không marketing.
3. ~~Tool cài skill~~ Đã chốt: AI coding tool của học viên (ba tool Winnie nêu); lesson dùng nhãn chung.
4. ~~Ví dụ cho Open~~ Đã nhận câu chuyện của Winnie (xem Structure mục 1). `[to confirm]` Winnie xem lại bản kể lại trong lesson.
5. ~~Hai bước kiểm tra thêm~~ Đã chốt (mình quyết theo đề nghị của Winnie, 2026-10-17): đưa cả hai vào bài. Dấu hiệu bên ngoài (tác giả, sao, lần cập nhật cuối, license) ở Theory (b). Clone vào một folder mới, tách khỏi dự án thật, là bước đầu của Practice. Lý do: học viên không đọc được code, nên tách riêng folder là lớp bảo vệ chắc nhất và gần như không tốn thời gian, vì clone bằng GitHub Desktop đã tạo folder mới. Cả hai vào cheat sheet ở Bridge.
6. Repo template của Winnie chưa hiện license. Winnie thêm file LICENSE trên GitHub trước buổi học (cách làm ở phản hồi trong chat). `[to confirm]` sau khi thêm.

## Sources
- Chuẩn Agent Skills (SKILL.md), cách cài: [Parallel](https://parallel.ai/articles/what-are-agent-skills.md), [Firecrawl](https://www.firecrawl.dev/blog/agent-skills), [OpenSkills](https://docsearch.algolia.com/mcp/docs/repo/numman-ali/openskills). Cờ lệnh CLI `[to confirm]` bằng README chính thức.
- Rủi ro khi cài skill của người khác (nghiên cứu của hãng bảo mật, phương pháp khác nhau, không so sánh trực tiếp): "Agent Skills in the Wild" (31.132 skill, 26,1% có lỗ hổng); Snyk "ToxicSkills" (khoảng 4.000 skill, 13,4% có vấn đề nghiêm trọng); ESET H1 2026 (khoảng 900.000 skill, hơn 3.000 skill độc hại). Qua [forkast.news](https://forkast.news/ai-agent-skills-are-the-new-supply-chain-attack-vector-and-most-have-never-been-vetted), [expertinsights.com](https://expertinsights.com/news/1-in-300-ai-agent-skills-is-directly-malicious-eset-research-finds), [SafeDep](https://safedep.io/agent-skills-threat-model/). Mới đọc tóm tắt, `[to confirm]` bằng báo cáo gốc trước khi đưa số lên slide.
- License mở: [awesome-shadcn-ui](https://github.com/birobirobiro/awesome-shadcn-ui), kiểm tra license từng repo.
- Quy trình "feed markdown cho AI rồi đối chiếu với dự đoán" là cách dạy của Winnie, không có nghiên cứu hỗ trợ.

## Assets (ảnh chụp màn hình, đã lưu trong `../assets/`)
| File | Hiển thị gì | Dùng ở đâu |
|---|---|---|
| `lesson-5-repo-page-signals.png` | Trang một repo công khai: số sao, fork, license, commit gần nhất, README, thẻ topic | Theory (b) và (c): đọc trang repo, các dấu hiệu bên ngoài |
| `lesson-5-template-repo-use-this-template.webp` | Trang một template repo có nút "Use this template", thư mục demo và README | Theory (d) và Practice: lấy repo làm template |
| `lesson-5-showcase-user-flow-swimlane.webp` | User flow swimlane (traveler, app, local, companion) do diagram skill dựng, từ demo case | Open: kết quả của câu chuyện |
| `lesson-5-github-marketplace-home.webp` | Trang GitHub Marketplace với mục Apps và Actions | Theory (b): marketplace là nơi tìm gì |

- Đã chốt 2026-10-17: giữ nguyên tên tool và tên tài khoản trong ảnh chụp. Chữ trong lesson và slide vẫn dùng nhãn chung, chỉ ảnh giữ nguyên.
- Ảnh 2 là repo của Winnie và là repo template cho Practice.
- GitHub Marketplace trong ảnh 3 chỉ có Apps và Actions, không có mục skill. Vì vậy lesson không nói "marketplace có skill". Skill được tìm bằng GitHub search, awesome list hoặc trang riêng của từng tool `[to confirm]`.

## Limitations
- AI chat tool diễn giải file markdown không bảo đảm file an toàn. ESET cảnh báo chỉ dẫn độc hại có thể nằm ngay trong README. Bài nói rõ điều này và dạy học viên coi bước feed markdown là một lớp kiểm tra, không phải lớp duy nhất.
- Học viên không đọc được code, nên chỉ nên dùng repo có số sao và lần cập nhật hợp lý, và không đưa key hay file thật vào folder vừa clone.
