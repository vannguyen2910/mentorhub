# AI Design Workflow: Plan

*Cập nhật 2026-10-30: practice là chuỗi việc làm ở nhà (khoảng 4 giờ mỗi tuần), buổi practice trên lớp làm tiếp và chấm; synthesis dạy sớm ở lesson 2; phỏng vấn user thật. Các file khác chưa cập nhật theo (xem mục 4).*

*Cập nhật 2026-10-26: cấu trúc 12 buổi xen kẽ theory và practice, không còn Check point. Bản trước ở git; bản 14 session ở `_archive/plan-2026-10-22-14-session.md`; bản cũ hơn ở `_archive/00-plan-full-2026-10-07.md`.*

**Trong file này**
1. [Focus now](#1-focus-now)
2. [The course at a glance](#2-the-course-at-a-glance)
3. [Key decisions](#3-key-decisions)
4. [Still open](#4-still-open)
5. [Where things are](#5-where-things-are)

> **Nguồn lộ trình:** file này là nguồn chuẩn cho cấu trúc từ 2026-10-26. Trang Notion có thể còn ghi cấu trúc cũ (9 buổi nội dung và 3 Check point); cần cập nhật Notion cho khớp.

---

## 1. Focus now

Làm theo thứ tự.

| # | Việc | Trạng thái |
|---|---|---|
| 1 | **Lesson 1:** xác nhận số liệu Figma 36/35/29 trong báo cáo đầy đủ trước khi dạy; dựng lại deck | File xong; deck chưa dựng |
| 2 | **Lesson 2:** lesson và slide outline đã viết lại (2026-10-26); xem lại các ví dụ `bản nháp`; **thêm synthesis** (chuyển từ lesson 3, 2026-10-30) và phỏng vấn user thật; dựng deck | File cần viết lại phần synthesis; chờ Winnie xem lại |
| 3 | **Lesson 3:** sửa lesson và slide (competitor đầy đủ đã chuyển sang lesson 2; thêm persona, journey map, opportunity, insight hub; synthesis rút gọn thành phần ôn) | Đã có desk research và đề xuất cấu trúc 90 phút (`reference/ai-in-insights.md` mục 6, 2026-10-27); đã viết lại 2026-10-30 (synthesis sang lesson 2, thêm package); cần soạn persona mẫu cho activity |
| 4 | **Lesson 4, 5, 6** (mỗi lesson gộp hai lesson cũ), theo thứ tự | Chưa bắt đầu |
| 5 | Hướng dẫn facilitation một trang cho practice P1 đến P5 và buổi wrap-up | Chưa bắt đầu |
| 6 | Lớp chạy thử: kiểm tra khoảng 4 giờ làm ở nhà mỗi tuần (mục tiêu 2026-10-30), nhất là tuần 2 và 6; theory lesson 2 (56 phút, nay thêm synthesis), lesson 3 và 6 có quá tải không | Sau lớp đầu |

---

## 2. The course at a glance

**Ai học:** UI/UX và product designer mức mid và senior, lớp 7 đến 8 người.
**Học xong được gì:** một workflow thiết kế có AI dùng lại được, từ business question đến prototype đã test. Output mỗi bước là input của bước sau, và gom vào một Knowledge Hub.

**Nhịp học (2026-10-30):** 6 tuần, mỗi tuần hai buổi 90 phút. Một buổi **theory** (khái niệm, activity ngắn). Sau đó học viên làm **practice ở nhà**: một chuỗi việc trên case của mình, khoảng 4 giờ mỗi tuần, mỗi bước cho ra một file và đầu ra của bước trước là đầu vào của bước sau. Buổi **practice trên lớp** (90 phút): học viên làm tiếp phần còn dang dở nếu còn thời gian, rồi Winnie chấm kết quả. Cách chấm chưa quyết (mục 4). Không có Check point.

| Tuần | Theory | Practice | Output |
|---|---|---|---|
| 1 | **Your Design Process, with AI**: nghề đang đi đâu, AI trong Double Diamond, data safety | Dựng case folder, data rules, hub | Case folder, hub |
| 2 | **Discover the Problem**: principles, break the brief, hiểu người dùng, phỏng vấn và **synthesis** (chuyển từ lesson 3) | Ở nhà: `principles.md`, research plan (gồm scope, UX observation, assumption, research questions, competitor), phỏng vấn user thật, ẩn danh transcript, synthesis, đưa insight lên hub và nối về business question | `research-questions` (scope và câu hỏi), `ux-audit`, `assumption`, `competitor-analysis`, synthesis, insight trên hub |
| 3 | **Insights You Can Trust**: persona, journey map, opportunity (mỗi dòng dẫn về quote có ID); synthesis chỉ ôn lại vì đã học ở tuần 2 | Trên insight của chính học viên (từ tuần 2): `personas.md`, `journey-map.md`, `frame-opportunity.md`, một trang cho lead, entry insight hub; nội dung có trên hub và mỗi dòng nối về quote ID | Evidence pack, **problem brief** |
| 4 | **Explore Ideas**: hypothesis, How might we, Solution Tree, sketch giấy rồi AI, chọn hướng | Hypothesis, Solution Tree, danh sách giải pháp có ưu tiên, concept sketch, chọn hướng bằng principle check, **user flow** `[to confirm]` (bản draft của Winnie chưa có hypothesis, How might we và flow) | Hướng đã chọn, user flow |
| 5 | **AI Prototyping**: design system, pattern, template, rules file | Build prototype main flow | Prototype sẵn sàng test, có thể là final design |
| 6 | **Test with Real Users**: metrics, test plan, phân tích kết quả | Test với peer trong **một ngày**, rồi buổi 12 **reflection và wrap-up** | Prototype đã test, hub đầy đủ |

**Cần nhớ:**
- Sơ đồ sáu tuần trên hub dựng từ `assets/diagrams/ai-design-workflow-six-weeks.swimlane.json` (không đọc từ file này): đổi kế hoạch thì sửa cả bảng ở đây và file JSON đó.
- Tuần 4, 5, 6 mỗi buổi theory gộp hai lesson cũ; chỉ giữ khái niệm lõi, phần còn lại thành cheat sheet và được coaching ở practice. Tuần 2, 3 và 6 nặng nhất; tuần 2 nặng thêm vì có cả synthesis.
- Mỗi practice kết thúc bằng hai bước cố định (từ bản draft 2026-10-30): nội dung đã có trên hub, và mỗi dòng nối về nguồn (quote, requirement, business question). Practice 6 còn thiếu bước "linked" ở bản draft.
- Transcript thô phải ẩn danh và có consent trước khi đưa cho AI; bản draft practice 2 chưa có bước này.
- Practice 1 có thêm hai bước tuỳ chọn: push lên Git và bật trang live. Output "ready-folder với context" không phụ thuộc vào hai bước này.
- Define rải theo mạch: problem brief ở cuối tuần 3, hypothesis đầu tuần 4, metrics ở tuần 6. Không còn lesson handoff và measurement plan (bỏ 2026-10-26).
- Tên gọi: buổi theory là "lesson" (T1 đến T6), buổi practice là "practice" (P1 đến P6). File lesson hiện còn ghi "buổi N" theo số lesson; đổi khi sửa lần tới.
- Chi tiết từng lesson nằm trong file lesson, practice và `lesson-N-details.md` (Lesson 1, 2, 3, 5); bản cũ cho Lesson 4 và 6 đến 9 ở `_archive/lesson-details-pre-split-2026-10-30.md` cho đến khi viết lại.

**Theo dõi tiến bộ:** KNOW (giải thích khái niệm bằng lời của mình), DO (một file trong case folder), SHOW (trình bày và review chéo ở practice và buổi wrap-up). Thêm **learning log** (`_personal/learning-log.md`, riêng tư): mỗi practice kết thúc bằng ba phút ghi ba dòng và một câu reflection; buổi wrap-up đọc lại để tìm điều lặp lại. Đã áp dụng cho P1 đến P3; P4 đến P6 chưa viết nên chưa có bước này. Khung: skill `learning-loop`.

---

## 3. Key decisions

| Chủ đề | Quyết định |
|---|---|
| Vai trò của design | **Partner** của product và business, bắt đầu từ business question. Brief có sẵn là điểm xuất phát, không phải thứ cần sửa. Không gọi PO, PM, BA là rào cản; nói "product and business". |
| Kết quả chính | Một workflow AI dùng lại được. Không dạy prompt tips hay tool. |
| Nhịp học | Theory rồi practice mỗi tuần (xem mục 2). Mỗi lesson: ice breaker, theory, activity khoảng 5 phút, hỏi đáp. Luyện tập là chuỗi việc **ở nhà** (khoảng 4 giờ mỗi tuần, quyết định 2026-10-30); buổi practice trên lớp làm tiếp phần dang dở và chấm. Lesson 1 có theory dài hơn (44 phút). Không có Check point. |
| Chấm điểm | Winnie chấm. Benchmark và cách chấm chưa quyết; brainstorm sau (mục 4). |
| Case | Mỗi người một case của chính mình; case mẫu của chương trình là phương án dự phòng. Tài liệu bảo mật được ẩn danh trước. |
| Data safety | Dạy ở buổi 1: ba loại tài liệu (an toàn, hỏi trước, không đưa vào tool công khai), bốn thói quen, học viên tự viết data rules. |
| Discover | Không role-play: AI không bao giờ đóng PO hay user. Dùng câu hỏi gửi business bằng văn bản và phỏng vấn **user thật** của case (đổi từ peer, 2026-10-30; học viên phỏng vấn ở nhà trước buổi practice 2). Synthesis dạy ở lesson 2, không phải lesson 3. Transcript thô ẩn danh và có consent trước khi đưa cho AI. Principles đặt trước, AI chạy sau. |
| Access | Ba mức (full, limited, none). Outcome chưa xác nhận ghi là **assumed**. |
| Principles | Nielsen 10 làm nền, thêm nguyên tắc của tổ chức nếu có. |
| Gates | Bốn gate, 20 check (1a đến 4d), định nghĩa một lần ở `method.md` Part 3. |
| Đo lường | Lõi là usability metrics trước launch (Goals, Signals, Metrics). Business metrics hỏi product, ghi assumed. |
| Tool | Một AI chat tool từ lesson 1, một AI coding tool từ lesson 5. Lesson và slide dùng tên chung; tên cụ thể chỉ nằm ở `assets/templates/tools-to-bring.md`. |
| Toolkit | `workspace-template/toolkit/` là nguồn gốc duy nhất (quyết định 2026-10-28). Mỗi skill là một folder `toolkit/skills/<tên>/` (`SKILL.md`, `templates/`, `examples/`), script ở `toolkit/tools/`. Không còn đồng bộ từ skill `product-workspace`. Kế hoạch và kết quả: `_system/toolkit-refactor/toolkit-refactor-plan.md`. |
| Prototype | Học viên không viết code; AI coding tool làm. Mục tiêu lesson 5: prototype sẵn sàng test, có thể là final design. |
| Hub | Private mặc định, nằm trong case folder. Đưa lên GitHub là tuỳ chọn. |
| Định hướng nghề | Lesson 1 dành 18 phút cho hướng đi của nghề và ba con đường; số liệu có nguồn, năm, cỡ mẫu (`reference/research.md` Part 5). Học viên viết `my-direction.md` và xem lại ở buổi wrap-up. Chương trình không dạy thiết kế sản phẩm AI. |
| Đã bỏ | Lesson handoff và measurement plan; workflow lab (tài liệu cũ ở `assets/templates/workflow-kit/` giữ nguyên, không dùng trong lớp). Quyết định 2026-10-26. |
| Tên gọi | Mỗi ý một tên, định nghĩa ở `vocabulary.md`. Không dùng tên tool AI trong lesson. |

---

## 4. Still open

**Cần Winnie quyết:**
1. Nội dung practice P1 đến P6 và bài tập về nhà còn việc nào.
2. Capstone: mỗi người một case (nghiêng về hướng này, chưa chốt hẳn).
3. **Cách chấm điểm:** benchmark, tiêu chí, đạt hay chưa đạt hay điểm số. Winnie chấm; brainstorm sau.
4. **Buổi practice trên lớp** với 7 đến 8 học viên: mỗi người trình bày rồi bị chấm, hay chấm trước bằng file và buổi lớp chỉ sửa chỗ chưa đạt.
5. **Practice 4:** giữ hypothesis và How might we cùng Solution Tree, hay thay bằng bản draft; thêm user flow là chắc chắn.
6. **Practice 6:** người được test (peer hay user thật), metrics (Goals, Signals, Metrics) đặt ở bước nào, và bước sửa prototype sau finding.
7. **Lesson 2 có quá tải không** khi thêm synthesis vào theory (hiện 56 phút).

**Việc cần làm:**
- **Đồng bộ theo cách hiểu mới (2026-10-30), chưa làm:** `introduction.md` (Lộ trình), `README.md` (bảng Lessons), `assets/diagrams/ai-design-workflow-six-weeks.swimlane.json` (đang ghi practice là buổi làm trên lớp), bảng "Connection to the series" của từng lesson, và các practice sheet P1 đến P3 (đang chia theo phút trong buổi 90 phút, cần viết lại thành chuỗi việc ở nhà cộng phần làm tiếp và chấm trên lớp).
- **Đã làm (2026-10-30):** synthesis chuyển từ lesson 3 sang lesson 2 (lesson và slide outline của cả hai đã viết lại; Lesson 2 có 33 slide, theory khoảng 61 phút; Lesson 3 có 22 slide, thêm activity "persona có quote hay không" và slide package thành agent chuyển từ Lesson 2). Còn lại: soạn `assets/starter-files/course-case/persona-ai-draft.md` cho activity mới của Lesson 3, viết lại practice sheet P2 và P3, và thử thời lượng Lesson 2 với lớp thật.
- Thêm vào practice: bước ẩn danh transcript (P2), user flow (P4), hai bước "Hub" và "linked" ở cuối mỗi practice (P6 còn thiếu "linked").
- Dựng lại năm hình draft practice của Winnie (2026-10-30) theo style của khoá, nhãn thống nhất một ngôn ngữ, sau khi chốt các mục ở trên.
- Viết practice P3 đến P6 và thư mục `07-wrap-up` (chỉ có file practice) khi chốt nội dung; P1 và P2 đã có bản nháp. Hub hiện Lesson và Practice trong nhóm `Lessons` của `SUMMARY.md`, không hiện outline.
- Đổi nhãn "buổi N" thành "lesson N" trong các file lesson và slide outline; viết lại lesson 4 đến 11 cũ (bản cũ ở `_archive/lesson-details-pre-split-2026-10-30.md`).
- Sửa các trang còn nhắc Check point, handoff hoặc 9+3 buổi: `README.md`, `introduction.md`, lesson 1.
- Kiểm chứng ở Việt Nam: phỏng vấn 5 đến 8 designer hoặc hiring manager (`reference/research.md` Part 3).
- Dọn file cũ: `assets/templates/po-case-pack-template.md`, `assets/starter-files/course-case/po-case-pack.md`.
- Vẽ các flow còn thiếu: problem brief, ideation, prototype build, alignment check.
- Ba mẫu workflow từ designer khác (2026-10-30, chưa có nguồn công khai, nói rõ khi dạy): **Link** (requirement gắn vào element) đã vào Lesson 5 mục 3.5 và P5, sơ đồ `lessons/05-ai-prototyping/assets/ai-pattern-link.html`. Còn lại: **Render** (một file `.md` ra nhiều bản flow) vào Lesson 4 phần flow; **Route** (feedback thành implement ticket, có người duyệt và data rules) vào Lesson 6. Sơ đồ đã vẽ ở `assets/diagrams/ai-pattern-render.html` và `ai-pattern-route.html`; chuyển vào `assets/` của lesson khi viết Lesson 4 và 6. Thêm một slide tổng hợp ba mẫu ở buổi wrap-up.
- Làm template facilitator page cho phỏng vấn (câu hỏi, follow-up, ghi chú, timer) trước practice P2 và P3; chi tiết ở `reference/ai-in-discover.md`.

---

## 5. Where things are

Thư mục `learning/` (riêng tư, không lên site trừ các file có trong `SUMMARY.md`) giữ kế hoạch, research và method.

Danh mục từng file trong `learning/` (nguồn chính của việc gì, file nào đã cũ) nằm ở [`INDEX.md`](INDEX.md); không liệt kê lại ở đây.

**Ở nơi khác**

| Vị trí | Nội dung |
|---|---|
| `assets/templates/synthesis-hunt/` | Bộ activity "Săn lỗi" cho lesson 3: quote "Ăn Ngay", bản synthesis có lỗi cài sẵn, bảng lỗi cho giảng viên (không gửi học viên trước khi activity kết thúc) |
| `assets/templates/rule-break-hunt/` | Activity "Rule-break hunt" cho T5 (5 phút): màn hình `screen.html` có ba lỗi cài sẵn và đáp án giảng viên. Bản nháp, chưa thử. Kế hoạch: `learning/reference/lesson-5-activity-rule-break-hunt.md` |
| `assets/templates/handout-ai-design-workflow-buoc-1.md` | Giáo án một buổi thực hành (workflow audit, role card, baseline run). Chưa dùng trong 12 buổi; role card hợp với lesson 5 |
| `assets/references/claude-code-16-lessons-nhat-anh.md` | Ghi chú từ một video về cách dùng AI coding tool; tài liệu tham khảo, không thuộc khoá |
| `assets/templates/workflow-kit/` | Bộ mẫu cho học viên: step card, luật cho AI tool, propose first, prompt vocabulary, checklist, failure case |
| `workspace-template/` | Repo mẫu cho học viên (GitHub: `ai-product-workflow`) |
| `examples/` | Hai ví dụ làm sẵn: competitor analysis, user-voice synthesis |
| `README.md` | Thứ tự lesson, trạng thái, cách thêm lesson. Các lesson nằm ở `programs/ai-design-workflow/lessons/` |
| `_archive/` | Bản thay thế và bản trước khi dọn (có hậu tố ngày) |
