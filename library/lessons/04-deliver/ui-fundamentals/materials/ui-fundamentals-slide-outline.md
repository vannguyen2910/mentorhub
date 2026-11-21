# Slide Deck Outline: UI Fundamentals

> **Source of truth:** `ui-fundamentals-lesson.md`
> All content changes (activities, concepts, examples, timing) must be made there first, then reflected here.
> This file contains only slide-specific concerns: layout types, visual hints, kickers, structure, and speaker notes.

> **How to use this file**
> This outline is ready to hand to your own AI tool or process to generate the slide deck; the build prompt isn't included here.
> Speaker notes are written as short bullets, not prose: they're meant to be glanced at while teaching, not read.

---

## Session metadata

| Field | Value |
|---|---|
| Session title | UI Fundamentals |
| Session subtitle | Judging design decisions you didn't make |
| Instructor | Winnie Nguyen |
| Program | Private training. Follows Information Architecture Basics, precedes UI Foundations: Building in Figma |
| Level | Junior |
| Year | 2026 |
| Previous session | Information Architecture Basics. Output: sitemap and process map |
| Next session | UI Foundations: Building in Figma. Builds the chosen concept |
| Running example | Food delivery, order tracking screen. Same case as the senior track: four stages, actual job at waiting-for-delivery |
| Cover photo | A hand holding a phone showing a delivery tracking screen, seen slightly from behind. The viewer can tell something is being judged, not admired |
| Style reference | `../assets/style-reference-schematic.png` |

---

## Visual language

**This is a lesson about seeing. The deck has to be seen, not read.** A student who can recite "proximity means near equals related" and cannot spot a grouping failure has learned a sentence, not a skill. So almost every principle in this deck is shown as a specimen, and the words on the slide are labels for what the eye is already doing.

### Two registers, and the switch between them means something

**SCHEMATIC.** Abstracted UI: grey bars for text, geometric shapes for controls, no real words, no photography. This is the register for teaching a mechanism. Its whole value is that it removes content as a variable, so nobody can be distracted by whether the copy is good or the photo is nice. Only structure is left, and structure is what the five layers are about. Style reference: `../assets/style-reference-schematic.png`.

**REAL.** Fully rendered screens with real type, real colour, real images. This is the register for the tracking screen and the reveal. It is used wherever *attractiveness itself* is the subject, because a grey-bar wireframe cannot fool anybody and the whole reveal depends on students having been fooled.

**The rule: schematic teaches the mechanism, real shows what fools you.** Each layer runs schematic first, then real. Never mix the two registers inside one slide.

### Schematic drawing kit

| Element | How to draw it |
|---|---|
| Body text | Short horizontal strokes, `--ink-ghost`, 2px, round caps. Never real words. Vary length to imply content |
| Heading text | A thicker stroke (4px), `--ink-muted`, shorter than body runs |
| Primary button | The one filled element in a specimen: `--ink` fill, rounded rect |
| Secondary button | Outlined rounded rect, 2px `--ink-muted` |
| Input field | Outlined rounded rect, taller than a button, empty |
| Radio / checkbox | Circle outline. Selected = a small `--ink` dot inside |
| Image or map | Outlined rect, no fill. No icon inside, no mountain glyph |
| Specimen frame | 2px `--ink` hairline, corners rounded with `--radius-lg` like every Design System card, generous internal padding |
| Annotation | `--sienna` arrows, brackets and measurement rules: the only colour in a specimen |
| Measurement labels | `--font-mono`, at least 18px, `--sienna` |

**Line-art rule (Design System).** Specimens follow the Design System illustration rule: 2px strokes, no fill, no gradient. The only exception is emphasis, which is an `--ink` filled shape, and the only colour is the one `--sienna` accent used for annotation. Colour appears elsewhere only in the REAL register and on the role chips of the "Roles, not palettes" slide, where colour is the subject.

### Rules for every specimen slide

1. **The frame separates specimen from slide.** Anything inside a hairline frame is a UI being examined. Anything outside it is the deck talking. Never let slide chrome bleed into a specimen.
2. **One accent, pointing at one thing.** `--sienna` annotates the element under discussion and nothing else; emphasis inside a specimen is an `--ink` fill. If two things are purple, the slide is making two arguments and should be two slides.
3. **No red X, no green tick, no "bad" and "good" labels.** Mark what is under discussion and let the student judge. The moment the slide grades the screen, it has done the work the student was supposed to do.
4. **COMPARE slides change exactly one variable.** Same content, same layout, one decision different. Two screens that differ in five ways teach taste. Two that differ in one teach a principle.
5. **Label comparisons in `--font-mono`, neutrally.** "24px" and "18px", not "wrong" and "right".
6. **Measurement is drawn, not described.** If the slide claims a gap is 24, the 24 is on the slide with a bracket. This is the habit that converts a junior's "I think" into "it's 3.9 and it needs 4.5".

### Asset production note

Less work than it looks. The schematic kit is one Figma component set reused across every diagram. The REAL register is one tracking screen built once in its broken state, plus five corrected variants and two effect versions (blurred, desaturated).

---

## Slide structure

> **90-minute version, 44 slides.**
> Arc: Open → The Frame → Layers 1 to 4 → The Reveal → Layer 5 → Close → Practice → Homework.
> Five teaching layers, each running the same four-beat pattern: the question it answers, the principle (schematic), the worked example (real), the sentence you say to a dev. That repetition is deliberate and should not be varied for interest.
> **The reveal sits at slide 30, not slide 4.** The Aesthetic-Usability Effect only works if students have already been caught by it in the opening. Do not move it earlier.
> **The tracking screen appears in every layer**, each time with all previous layers already corrected. By Layer 5 the students have watched one screen repaired in front of them. That cumulative build is the deck's spine and is also what proves the reading-order claim visually.
> Ten text-only slides out of 44, and half of those carry a small specimen. Every remaining slide shows something.
> **Pacing:** 44 slides across 70 minutes of teaching, so roughly 1.6 minutes each. That is faster than a text deck and it should be. A specimen slide is looked at, not read, and several are questions answered in fifteen seconds. The slides that need to breathe are the map problem, the blur test, the Kurosu finding and the closing six-state progression; take time on those and move briskly through the rest.
> Every slide lists on-slide content separately from speaker notes; keep the two from merging back together when building the deck.

---

## 1. Open

---

### COVER
- Year: 2026
- Day label: After Information Architecture
- Title: UI\n*Fundamentals*
- Subtitle: Judging design decisions you didn't make.
- Author: Winnie Nguyen
- Right panel photo: A hand holding a phone at a slight angle, delivery tracking screen visible. Judged, not admired.
- Speaker notes:
  > Hôm nay không nói về cách làm màn hình đẹp hơn.
  - Phụ đề của bài chỉ được giải thích ở cuối buổi.
  - Màn hình trên ảnh bìa đủ rõ để nhận ra là màn hình theo dõi đơn hàng, nhưng chưa đủ rõ để đánh giá.
  - Bài này dạy nhìn một màn hình theo một thứ tự cố định thay cho nhìn bằng cảm giác.
- Ví dụ: Không cần. Slide mở đầu, chưa có khái niệm.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: REAL. Photograph, warm light, slightly overhead. The screen readable enough to identify as a tracking screen, not readable enough to evaluate.

---

---

### STATEMENT · The split
- Kicker: Before we begin
- Title: Which *concept*\nwould you pick, and *why?*
- On-slide: The mentee's 2 to 3 concepts as placeholders. Instruction: **Pick one by instinct. Give the reason in one sentence.**
- Speaker notes:
  > Chọn một concept theo cảm giác và nói lý do trong một câu.
  - Mentee chọn một concept, giảng viên chọn một concept khác, và mỗi người nêu lý do của mình.
  - Hai lý do đều dựa trên cảm giác nên không có cách nào phân xử giữa chúng.
  - Sự bất đồng này chưa cần lời giải và được mở lại ở phần Reveal.
- Ví dụ: Không cần. Dùng concept của mentee.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: 2 to 3 neutral `.ph` placeholders labelled "concept 1/2/3". No ranking, nothing that makes one look chosen. The only colour is `--ink`.

---

## 2. The Frame

---

### DIAGRAM · Two gulfs
- Kicker: The frame
- Title: Making moved.\n*Judging didn't.*
- On-slide: LEFT **Gulf of Execution** wanting → doing. RIGHT **Gulf of Evaluation** seeing → understanding
- Speaker notes:
  > Gulf of Execution là khoảng cách giữa điều bạn muốn làm và việc làm được nó. Gulf of Evaluation là khoảng cách giữa điều màn hình hiện ra và việc hiểu nó có nghĩa gì.
  - Norman mô tả hai khoảng cách này cho người dùng, ở đây áp dụng ngược lại cho chính designer.
  - Trước đây, làm ra một màn hình cần kỹ năng công cụ, thời gian và tay nghề, nên junior chưa thể làm ra sản phẩm như senior.
  - Bây giờ một câu lệnh đủ để tạo ra màn hình trông hợp lý, spacing ổn và đẹp mắt.
  - Chưa có gì làm cho việc nhìn ba màn hình và biết cái nào đúng trở nên dễ hơn.
  > Làm ra thì gần như miễn phí. Đánh giá thì chưa.
- Ví dụ: bản nháp (một designer ở team product nhận ba phương án màn hình thanh toán trong năm phút và mất cả buổi chiều mà vẫn không nói được vì sao chọn phương án nào)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC. Two identical gap diagrams side by side: a figure glyph on one bank, a screen glyph on the other, the gap drawn as a measured span. LEFT span almost closed, annotated in `--sienna`. RIGHT span at full original width, same annotation style, unchanged. The two spans must be visibly the same drawing so the difference reads as width alone.

---

### STATEMENT · Where the value went
- Kicker: The consequence
- Title: Producing is no longer\nthe thing you're *paid for.*
- On-slide: nothing
- Speaker notes:
  > Làm ra màn hình không còn là thứ bạn được trả tiền để làm.
  - Giá trị từng nằm ở việc làm ra vì làm ra là thứ khan hiếm, bây giờ không còn như vậy.
  - Giá trị chuyển sang việc đánh giá, vì đánh giá là thứ vẫn khan hiếm.
  - Điều này khó nghe với người có chức danh designer và dành cả ngày để làm ra sản phẩm, nên slide được để trống.
  > Đánh giá cần những tiêu chí bạn gọi được tên. Phần còn lại của buổi này là các tiêu chí đó.
- Ví dụ: Không cần. Slide chuyển ý, chưa giới thiệu khái niệm mới.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Deliberately blank. The only fully empty slide in the deck, and it should feel like it. No specimen, no diagram, no accent.

---

### STATEMENT · The dev thread
- Kicker: How you'll know it worked
- Title: Every layer today ends\nin a sentence you could\nsay to a *developer.*
- On-slide: Not a rationale. A sentence.
- Speaker notes:
  > Mỗi layer hôm nay kết thúc bằng một câu bạn nói được với developer. Không phải một lập luận thiết kế, chỉ là một câu.
  - Hiểu một layer không phải là áp dụng được nó mà là nói được vì sao, với một người không quan tâm đến design.
  - Nhiều junior designer thua những cuộc tranh luận mình đúng, vì thứ duy nhất họ có trong tay là "trông đẹp hơn".
  - Câu nói với developer dùng ngôn ngữ của ràng buộc và chi phí chứ không dùng ngôn ngữ của cảm giác.
  > Khi phải bảo vệ một quyết định, câu trả lời của bạn có bỏ được chữ "trông" không?
- Ví dụ: bản nháp (developer hỏi "sao khoảng cách này là 24 mà không phải 20?" và designer chỉ trả lời được "nhìn thoáng hơn")
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC. A small empty speech bubble in `--sienna` outline, sized for one short sentence, pointing at a schematic screen fragment. The bubble stays empty here; it gets filled five times later in the deck. Reuse this exact bubble on every dev sentence slide.

---

### DIAGRAM · The Decision Stack
- Kicker: The instrument
- Title: Five layers,\nin *reading order.*
- On-slide: **01 · Space** what belongs with what · **02 · Hierarchy** what gets read first · **03 · Type** how it stays readable · **04 · Colour** what's the one thing to do · **05 · Component** why does this exist
- Speaker notes:
  > Năm layer này đi theo thứ tự đọc, không theo thứ tự quan trọng.
  - Mắt nhận ra nhóm nội dung trước, rồi đến thứ bậc, rồi chữ, rồi màu nhấn mạnh, và component là thứ cuối cùng được nhận ra.
  - Nhờ vậy bạn kiểm tra bài bằng cách nhìn chứ không phải nhớ một danh sách.
  - Thứ tự này cũng đi từ quyết định mang tính cấu trúc nhất đến cục bộ nhất, nên lỗi tốn kém nhất được bắt trước.
  - Một màn hình lỗi nhóm thường bị mô tả là "rối", và đổi màu hay đổi font thì màn hình vẫn rối.
  > Một công cụ duy nhất. Hôm nay nó được đưa vào ba thứ khác nhau.
- Ví dụ: bản nháp (một màn hình danh sách đơn hàng bị mô tả là "rối" và được sửa bằng cách đổi màu, trong khi lỗi nằm ở việc nhóm)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC. One schematic screen shown exploded into five stacked transparent planes, each plane isolating what that layer governs: plane 1 only the gaps, plane 2 only the size and weight differences, plane 3 only the type runs, plane 4 only the filled shapes, plane 5 only the component outlines. Numbered down the side in `--font-mono`. This is the deck's key image; it returns as a small locator on every layer divider.

---

## 3. Layer 1 · Space and Layout

---

### SECTION DIVIDER · Layer 1
- Kicker: Layer 01
- Title: SPACE AND\nLAYOUT
- On-slide: What belongs with what?
- Speaker notes:
  - Hầu hết màn hình của junior lỗi ở layer này.
  - Ít ai chẩn đoán đúng ở đây, vì lỗi nhóm thường được cảm nhận là "màn hình trông rối".
- Ví dụ: Không cần. Slide chia phần.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC. The five-plane stack from the previous slide, small, upper right, with plane 1 in `--sienna` and the rest ghosted. Same locator treatment on all five dividers.

---

### COMPARE · Proximity
- Kicker: The principle
- Title: Spacing is the first *meaning.*
- On-slide: Two specimens. Identical elements. Only the gaps differ. Mono labels: **8 / 8 / 8** and **8 / 24 / 8**
- Speaker notes:
  > Mỗi bên bạn thấy mấy nhóm?
  - Bên trái đọc thành một danh sách sáu mục, bên phải đọc thành hai nhóm ba mục, dù cả hai đều gồm sáu phần tử giống nhau.
  - Proximity không phải sở thích mà là cách thị giác hoạt động trước khi chú ý có ý thức xuất hiện.
  - Vì vậy khoảng cách là ý nghĩa đầu tiên trên màn hình.
  > Khoảng cách được đọc trước bất kỳ chữ nào.
  > Trên màn hình của bạn, bạn thấy mấy nhóm, và có đúng số nhóm bạn định không?
- Ví dụ: có (sáu thanh giống nhau với gap 8/8/8 và 8/24/8, trong lesson)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC, side by side in matched frames. Six identical grey bars in each. LEFT evenly spaced. RIGHT with one 24px gap in the middle. The gaps themselves annotated with `--sienna` measurement brackets. Nothing else differs, including bar lengths.

---

### COMPARE · Common region
- Kicker: The principle
- Title: A boundary *beats*\nproximity.
- On-slide: Two specimens. LEFT: two bars close together, two far. RIGHT: the far pair enclosed in one card, the close pair split across a card edge
- Speaker notes:
  > Trong mỗi bên, mục nào đi cùng mục nào?
  - Câu trả lời đảo chiều chỉ vì thêm một đường biên.
  - Hai mục cách xa nhau nhưng nằm trong cùng một card được đọc là liên quan hơn hai mục gần nhau nhưng nằm hai bên mép card.
  - Lỗi lặp lại mà luật này giải thích là thêm đường kẻ hoặc border khi vấn đề thật ra nằm ở spacing.
  - Border là công cụ mạnh, và khi dùng để vá lỗi spacing thì nó thêm tín hiệu nhóm thứ hai, hai tín hiệu này sẽ cãi nhau.
  - Phần lớn junior chưa từng nghe luật này.
  > Đường kẻ nào trên màn hình của bạn đang sửa một lỗi spacing?
- Ví dụ: bản nháp (một designer thêm đường kẻ giữa mọi dòng của danh sách đơn hàng cho "gọn", và danh sách vẫn rối vì khoảng cách giữa các nhóm chưa đúng)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC. Same bars in both frames, same positions. RIGHT adds one hairline card boundary in `--sienna`. The point is that only the boundary was added and the reading changed completely.

---

### DIAGRAM · The 8pt scale
- Kicker: The rule
- Title: Gaps in multiples of *eight.*
- On-slide: 8 · 16 · 24 · 32 · 40 · 48
- Speaker notes:
  > Mọi khoảng cách là bội số của 8. Hết luật.
  - Giá trị của luật không nằm ở thẩm mỹ mà ở chỗ nó biến một câu hỏi có vô hạn đáp án thành một câu hỏi có sáu đáp án.
  - "24 hay 25?" không còn là câu hỏi để mỗi người có một ý kiến.
  - Vì vậy nó cũng không còn là chuyện để tranh luận với developer, và đó là phần lớn lý do nên dùng nó.
  - Khoảng cách 25 trên slide nằm lệch khỏi các vạch chia, và chính các vạch chia nói điều đó.
  > Màn hình của bạn có bao nhiêu giá trị gap khác nhau, và giá trị nào không nằm trên thang?
- Ví dụ: bản nháp (một màn hình có các gap 12, 20, 25 và 30, sau khi đưa về 8, 16, 24 và 32 thì không còn gì để tranh luận với developer)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC. A schematic screen with a `--sienna` measurement rule running down its left edge, every gap bracketed and labelled in mono. One gap deliberately at 25 and labelled 25, sitting visibly off the rule's tick marks. Do not mark it wrong; the tick marks do that.

---

### COMPARE · Worked: the tracking screen
- Kicker: Food delivery
- Title: Nothing removed.\nJust *regrouped.*
- On-slide: The tracking screen, before and after, spacing only
- Speaker notes:
  > Mình đã đổi gì trên màn hình này?
  - Đây là lần đầu bạn thấy màn hình thật, và nó quay lại ở mọi layer tiếp theo.
  - Trạng thái đơn hàng và giờ giao dự kiến thuộc cùng một nhóm nhưng thường không được đặt cạnh nhau như một nhóm.
  - Tên shipper nằm đủ gần phần nội dung đơn hàng để bị đọc như một phần của nó.
  - Đáp án là "khoảng cách", vì phần tử, số lượng và nội dung chữ đều giữ nguyên.
  > Cùng phần tử, cùng số lượng, cùng chữ. Chỉ khác khoảng cách.
- Ví dụ: có (màn hình theo dõi đơn hàng giao đồ ăn, trong lesson)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: REAL, both sides fully rendered. Identical content in both. The changed gaps marked with `--sienna` brackets on the AFTER only. Keep every other property identical between the two, including image crop, so the eye has nowhere else to go.

---

### STATEMENT · Dev sentence 01
- Kicker: Say this
- Title: *"Those two are in the same\ngroup, so the gap is 8. The next\ngroup starts at 24. It's the scale,\nnot my preference."*
- On-slide: the corrected specimen, small, beside the quote
- Speaker notes:
  > "Hai phần này cùng nhóm nên gap là 8. Nhóm tiếp theo bắt đầu ở 24. Đó là thang chia, không phải sở thích của mình."
  - Câu này loại gu của designer ra khỏi lập luận.
  - Đọc to lần đầu thấy lạ, và cảm giác lạ đó là một phần của việc tập.
- Ví dụ: có (câu nói với developer của Layer 1, trong lesson)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: The empty speech bubble from the frame section, now filled with this sentence, pointing at a small SCHEMATIC fragment showing the two gaps. Same bubble, same position, on all five dev sentence slides so they read as a series.

---

## 4. Layer 2 · Hierarchy

---

### SECTION DIVIDER · Layer 2
- Kicker: Layer 02
- Title: HIERARCHY
- On-slide: What gets read first?
- Speaker notes:
  - Hierarchy không phải là "làm thứ quan trọng to hơn".
  - Layer này trả lời câu hỏi cái gì được đọc đầu tiên.
- Ví dụ: Không cần. Slide chia phần.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Five-plane locator, plane 2 in `--sienna`.

---

### DIAGRAM · Four levers
- Kicker: The principle
- Title: Size is *one* of four.
- On-slide: **01 · Size** · **02 · Weight** · **03 · Colour** · **04 · Space**
- Speaker notes:
  > Size mới chỉ là đòn bẩy dễ thấy nhất.
  - Hierarchy có bốn đòn bẩy: size, weight, colour và space.
  - Một màn hình cùng cỡ chữ vẫn có thể có hierarchy hoàn hảo nếu ba đòn bẩy còn lại làm việc, còn một màn hình có năm cỡ chữ có thể không có hierarchy nào.
  - Theo Von Restorff, phần tử khác biệt với xung quanh sẽ được chú ý, nên mức nhấn mạnh là một ngân sách cố định.
  > Ba nút primary nghĩa là không có nút primary nào.
  > Màn hình của bạn đang tiêu bao nhiêu ngân sách nhấn mạnh, và dành cho thứ gì?
- Ví dụ: bản nháp (màn hình đăng ký có ba nút nền màu là "Đăng ký", "Đăng nhập" và "Xem demo", và người dùng không biết bấm nút nào trước)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC. Four small specimens in a row, identical content in each, each one establishing the same hierarchy using only one lever. Fourth specimen uses space alone and should be the most surprising. Bottom of slide: a fifth specimen using all four at once on three different elements, visibly failing.

---

### COMPARE · Two firsts
- Kicker: The failure mode
- Title: Which one is\n*primary?*
- On-slide: LEFT: one filled button, one outlined. RIGHT: two filled buttons. Ask the question.
- Speaker notes:
  > Nút nào là primary?
  - Lỗi không phải là quá nhiều cỡ chữ mà là hai phần tử cùng cố gắng được đọc đầu tiên.
  - Ở bên phải, câu hỏi này không có đáp án, và chính điều đó là bằng chứng của vấn đề.
  > Nếu bạn không nói được phần tử nào được đọc đầu tiên trên concept của mình, concept đó không có hierarchy. Nó chỉ có sự đa dạng.
  - Phần practice sẽ tìm lỗi này trên các concept của chính bạn.
- Ví dụ: bản nháp (màn hình xác nhận đơn có "Đặt hàng" và "Thêm voucher" cùng nền màu)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC. Matched specimens. LEFT has exactly one `--ink` filled element. RIGHT has two. No labels, no marks. The slide asks the question and refuses to answer it.

---

### IMAGE · The blur test
- Kicker: A tool you can keep
- Title: The *hierarchy* survives blur.
- On-slide: The tracking screen, heavily blurred
- Speaker notes:
  - Blur bỏ nội dung và giữ cấu trúc, nên cái còn nhìn thấy là cái người dùng thấy trong nửa giây đầu.
  > Nếu không có gì nổi lên khi bị làm mờ, thì không có gì nổi lên.
  - Bản làm mờ được đặt cạnh bản rõ ở cùng kích thước và vị trí để so trực tiếp.
  - Phép thử này không tốn gì và dùng được mãi trên mọi màn hình, kể cả concept của chính mình.
  > Khi concept của bạn bị làm mờ, cái gì còn lại?
- Ví dụ: có (màn hình theo dõi đơn hàng ở bản làm mờ, trong lesson)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: REAL. The tracking screen at a heavy gaussian blur, full bleed or near it. No annotation at all on this slide. The next click reveals the sharp version at the same size and position for direct comparison.

---

### COMPARE · Worked: the map problem
- Kicker: Food delivery
- Title: The prettiest is *least useful.*
- On-slide: The tracking screen. Beside it, the actual job: *"let me stop fearing it's not coming."*
- Speaker notes:
  > Công việc thật của màn hình này là: "cho tôi hết lo đơn không đến."
  - Đây là cả buổi học gói trong một màn hình.
  - Bản đồ thường là phần tử to nhất và nhiều màu nhất, nhưng lại là thứ ít giúp ích nhất ở đây.
  - Thứ trả lời được nỗi lo là trạng thái đơn và lời hứa app sẽ báo khi có thay đổi.
  - Một chiếc xe máy chạy trên bản đồ chủ yếu cho người ta thứ để nhìn trong lúc vẫn lo.
  - Bản junior dẫn bằng bản đồ vì độ hấp dẫn là tiêu chí duy nhất họ có.
  > Bằng chứng nói hãy dẫn bằng sự trấn an, chứ không phải bằng sở thích.
- Ví dụ: có (màn hình theo dõi đơn hàng, với job "let me stop fearing it's not coming", trong lesson)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: REAL, both sides, spacing already corrected from Layer 1 so the cumulative build is visible. BEFORE: map dominant. AFTER: status and the notification promise dominant, map reduced to a supporting band. The actual-job quote sits outside both frames in `--sienna`, with a thin line to the element that answers it in the AFTER.

---

### TWO-COLUMN · Two laws you'll hear quoted wrongly
- Kicker: Scope check
- Title: Every rule has a *scope.*
- On-slide: LEFT **Hick's Law** "reaction time among simple, unfamiliar, equally likely options" / *Not* a scan of a labelled, grouped menu. RIGHT **Miller's 7±2** "immediate memory span, mostly about chunking" / *Not* a limit on nav items. Recognition, not recall.
- Speaker notes:
  > Một luật có phạm vi áp dụng. Kiểm tra phạm vi trước khi viện dẫn.
  - Hick's Law mô tả thời gian phản ứng khi chọn giữa các lựa chọn đơn giản, không quen và gần như ngang khả năng.
  - Cách dùng sai phổ biến là "menu phải dưới năm mục", trong khi một danh sách 20 mục có nhóm và nhãn rõ thường thắng danh sách 8 mục không nhóm.
  - Nhóm và nhãn thắng việc giảm số lượng.
  - Miller đo trí nhớ tức thời và bài báo chủ yếu nói về chunking, còn các mục trên thanh điều hướng đang nằm trên màn hình để đọc chứ không phải để nhớ.
  - Đó là recognition chứ không phải recall.
  > Designer viện dẫn một luật không áp dụng thì thua tranh luận và mất một phần uy tín.
  > Gần đây bạn nghe luật nào được dùng làm lập luận, và nó có đúng phạm vi không?
- Ví dụ: bản nháp (trong buổi review, một PM nói "Miller 7±2 nên menu chỉ được 7 mục")
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC, one small specimen per column proving the counter-case. LEFT: an ungrouped list of 8 bars beside a grouped, labelled list of 20, the 20 visibly easier to parse. RIGHT: a nav bar of 9 items that is obviously fine to read. The specimens carry the argument; the text only names it.

---

### STATEMENT · Dev sentence 02
- Kicker: Say this
- Title: *"The status is the primary.\nIf it can't be the biggest element,\nit has to be the highest contrast\none. It can't be neither."*
- On-slide: the corrected specimen, small, beside the quote
- Speaker notes:
  > "Status là primary. Nếu nó không thể là phần tử lớn nhất thì nó phải là phần tử có contrast cao nhất. Nó không thể thiếu cả hai."
  - Câu này nêu một ràng buộc chứ không nêu một sở thích.
  - Vế "không thể thiếu cả hai" là vế kết thúc cuộc tranh luận.
- Ví dụ: có (câu nói với developer của Layer 2, trong lesson)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Series bubble, filled. Small SCHEMATIC fragment showing one dominant element among four.

---

## 5. Layer 3 · Type

---

### SECTION DIVIDER · Layer 3
- Kicker: Layer 03
- Title: TYPE
- On-slide: How does the reading order stay readable?
- Speaker notes:
  > Layer này không có luật nào được đặt tên đứng sau.
  - Không phải quyết định thiết kế nào cũng có một bài báo tâm lý học bên dưới, và một phần là tay nghề theo quy ước.
  - Giả vờ có sẽ khiến bạn đi tìm một trích dẫn mà bạn không có, và điều đó gây xấu hổ trước một kỹ sư.
- Ví dụ: Không cần. Slide chia phần.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Five-plane locator, plane 3 in `--sienna`.

---

### COMPARE · Three and two
- Kicker: The rule
- Title: Three sizes, two *weights.*
- On-slide: LEFT: seven sizes, several 2px apart, labelled in mono. RIGHT: three sizes and two weights, same content
- Speaker notes:
  > Hai cỡ chữ này, cỡ nào lớn hơn?
  - Màn hình của junior thường có sáu hay bảy cỡ chữ, phần lớn chênh nhau 2px và không truyền đạt gì.
  > Khác biệt mà mắt không phân biệt được một cách chắc chắn thì không phải tín hiệu hierarchy. Đó là nhiễu, lại còn thêm chi phí bảo trì.
  - Chọn tỷ lệ giữa các bước, rồi mọi chữ trên màn hình lấy giá trị từ thang đó. Logic này giống lưới 8pt: đưa ý kiến cá nhân ra khỏi quyết định.
  - Line height thuộc về cỡ chữ chứ không thuộc về khối chữ, nên nó nằm trong thang.
  - Độ dài dòng quyết định đoạn văn có được đọc hay không nhiều hơn loại font, vậy mà junior lại tập trung chỉnh font.
  > Màn hình của bạn có mấy cỡ chữ, và bao nhiêu cặp chênh nhau dưới 2px?
- Ví dụ: bản nháp (một màn hình cài đặt có cả 15px, 16px và 17px, và không ai trong team nhớ vì sao)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: This one uses real type rather than bars, since the subject is type. Matched frames, identical copy in both. Every size labelled in mono beside it. LEFT deliberately includes 15/16/17px so the indistinguishable pairs are visible as numbers but not as sizes. RIGHT shows the three-step scale with its line heights bracketed in `--sienna`.

---

### DIAGRAM · The diagnostic
- Kicker: When it goes wrong
- Title: The fourth size is *upstream.*
- On-slide: It's Layer 2, unresolved.
- Speaker notes:
  - Cần cỡ chữ thứ tư để làm một thứ nổi lên thường là dấu hiệu lỗi nằm ở layer 2.
  - Bạn đang chữa một vấn đề hierarchy bằng một giải pháp về chữ.
  - Hướng xử lý là quay lên trên ngăn xếp chứ không đi xuống.
  - Cùng một màn hình, thêm cỡ chữ thứ tư vẫn chưa rõ, còn đổi spacing thì rõ với ba cỡ.
  > Lần gần nhất bạn thêm một cỡ chữ để làm một thứ nổi lên, vấn đề thật nằm ở đâu?
- Ví dụ: bản nháp (một màn hình hồ sơ thêm cỡ chữ thứ tư cho tên người dùng, và vấn đề thật là tên đang cách quá gần phần mô tả)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC. The five-plane stack with a `--sienna` arrow travelling from plane 3 back up to plane 2. Beside it, one specimen shown twice: once "fixed" by adding a fourth type size and still unclear, once fixed by changing the spacing and clear at three sizes.

---

### STATEMENT · Dev sentence 03
- Kicker: Say this
- Title: *"Three sizes, two weights, all\non the scale. If I need a fourth,\nsomething upstream is wrong\nand I should fix that instead."*
- On-slide: the type scale, small, beside the quote
- Speaker notes:
  > "Ba cỡ, hai weight, đều nằm trên thang. Nếu mình cần cỡ thứ tư thì có gì đó ở phía trên đang sai và mình sửa chỗ đó."
  - Vế sau làm câu này đáng tin vì nó thừa nhận một điều kiện thất bại.
- Ví dụ: có (câu nói với developer của Layer 3, trong lesson)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Series bubble, filled. Small specimen of the three-step scale.

---

## 6. Layer 4 · Colour

---

### SECTION DIVIDER · Layer 4
- Kicker: Layer 04
- Title: COLOUR
- On-slide: What is the one thing to do here?
- Speaker notes:
  > Câu hỏi của layer này là "việc duy nhất cần làm ở đây là gì".
  - Không phải "bảng màu nào" và cũng không phải "cảm xúc nào".
- Ví dụ: Không cần. Slide chia phần.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Five-plane locator, plane 4 in `--sienna`.

---

### DIAGRAM · Roles, not palettes
- Kicker: The principle
- Title: Colour is a *job.*
- On-slide: Brand · Neutral · Success · Warning · Error, each with its surface and text values
- Speaker notes:
  - Junior thường chọn một bảng màu đẹp. Cách làm đúng là gán ý nghĩa cho từng màu rồi không dùng màu mang nghĩa đó cho việc khác.
  > Khi màu đỏ báo lỗi cũng là màu của nút chính, màn hình mất khả năng nói "lỗi".
  - Von Restorff lại xuất hiện, nên layer này ngắn: màu là đòn bẩy nhấn mạnh mạnh nhất, nên cũng dễ bị dùng phung phí nhất.
  - Nếu hành động chính không phải phần tử bão hoà duy nhất thì nó không phải hành động chính.
  > Mỗi màu trên màn hình của bạn đang làm đúng một việc nào?
- Ví dụ: bản nháp (màn hình thanh toán dùng đỏ cho nút "Thanh toán" và cũng dùng đỏ cho thông báo thẻ bị từ chối, nên người dùng nhìn thông báo lỗi như một nút)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Five role chips in a row, each drawn as an outlined rect with a 3px coloured stroke (the one slide where colour is the subject), showing its surface and text pairing with the ratio printed on it. Beneath: one schematic screen where the error colour is also the primary button, and an error message on the same screen that has visibly nowhere to go. Do not label it as an error; let the collision be seen.

---

### IMAGE · The desaturate test
- Kicker: A second tool you can keep
- Title: Is the hierarchy *still there?*
- On-slide: The tracking screen in greyscale
- Speaker notes:
  - Phép thử này đi cùng blur: blur hỏi cấu trúc có còn khi bỏ nội dung, thang xám hỏi hierarchy có còn khi bỏ màu.
  > Nếu hành động chính biến mất trong thang xám, thì màu đang làm toàn bộ công việc, và màn hình hỏng với bất kỳ ai không dựa được vào màu.
  - Đây cũng là phép kiểm tra accessibility rẻ nhất, chỉ cần bật một công tắc.
  - Bản có màu được hiện lại ở cùng kích thước và vị trí.
- Ví dụ: có (màn hình theo dõi đơn hàng ở thang xám, hai phiên bản: hierarchy còn và hierarchy mất)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: REAL. Tracking screen fully desaturated, full bleed or near it, no annotation. Next click restores colour at identical size and position. Two versions worth preparing: one where hierarchy survives, one where it collapses.

---

### COMPARE · One rule and a tool
- Kicker: Contrast
- Title: One rule and a *tool.*
- On-slide: WCAG 2.1 AA: **4.5:1** for body text, **3:1** for large text and anything that carries meaning. Two text samples with their measured ratios printed large. Check it, don't estimate it.
- Speaker notes:
  - Một quy tắc và thói quen chạy công cụ: accessibility cần một buổi riêng và không vừa trong mười phút.
  > Đây là cổng bắt buộc chứ không phải hướng dẫn, vì đó là quyết định duy nhất trên màn hình có đáp án đúng.
  - Một junior tranh luận bằng con số đã đo, thay vì sở thích, đang ở trong một cuộc trò chuyện hoàn toàn khác.
  - Chữ trạng thái trên màn hình theo dõi đơn thường là xám trung bình trên nền trắng, trượt ngưỡng một chút và không ai để ý vì màn hình trông êm.
  > Êm và không đọc được rất dễ bị nhầm với nhau.
  > Con số contrast của chữ phụ trên màn hình của bạn là bao nhiêu?
- Ví dụ: có (chữ trạng thái xám trên nền trắng của màn hình theo dõi đơn hàng, trong lesson)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Two real text samples side by side, deliberately similar. Make the failing one look pleasant. Ratios printed beneath each in large mono, `--sienna` on the failing number only. No X, no tick. The number is the verdict.

---

### STATEMENT · Dev sentence 04
- Kicker: Say this
- Title: *"Red is our error role. If we use\nit for the primary button we lose\nthe ability to show an error\non this screen."*
- On-slide: the role chips, small, beside the quote
- Speaker notes:
  > "Đỏ là role error của mình. Nếu dùng nó cho nút chính, màn hình này không còn cách nào để hiện lỗi."
  - Câu này nêu một khả năng bị mất chứ không phải một quy tắc bị phá, nên khó phản bác hơn.
- Ví dụ: có (câu nói với developer của Layer 4, trong lesson)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Series bubble, filled. Small specimen of the five role chips.

---

## 7. The Reveal

---

### IMAGE · Back to the start
- Kicker: The return
- Title: So why *that concept?*
- On-slide: The mentee's concepts again, the two picks ringed: the mentee's with "Lý do của bạn", the instructor's with "Lý do của mình"
- Speaker notes:
  > Bây giờ bạn vẫn chọn concept đó chứ, và vì sao?
  - Lý do viết ở đầu buổi được đọc lại.
  - Bạn thử trả lời trước với bốn layer từ vựng mà lúc đầu chưa có.
  - Câu trả lời thường tốt hơn lúc đầu, và sự cải thiện đó đáng được gọi tên trước khi sang phần reveal.
- Ví dụ: Không cần. Dùng concept của mentee.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: The three placeholders at full size, concept 1 and concept 3 ringed in `--sienna`, each with its one-sentence reason in `--ink-muted`.

---

### DIAGRAM · Kurosu and Kashimura, 1995
- Kicker: The finding
- Title: People believe attractive\nthings *work better.*
- On-slide: 252 participants · 26 ATM interface variations · appeal correlated more strongly with **perceived** ease of use than with **actual** ease of use
- Speaker notes:
  - Hitachi Design Center, 1995: 252 người đánh giá 26 biến thể giao diện ATM theo độ hấp dẫn và độ dễ dùng.
  - Độ hấp dẫn tương quan với độ dễ dùng cảm nhận mạnh hơn so với độ dễ dùng thực tế.
  - Tractinsky lặp lại thí nghiệm ở Israel, kỳ vọng yếu tố văn hoá làm hiệu ứng yếu đi, nhưng lại thấy nó mạnh hơn.
  > Designer cũng tin như vậy. Bạn cũng tin như vậy ở đầu buổi học.
  - Với người dùng, đây là điều có thật và hữu ích: thiết kế đẹp đổi được sự khoan dung, nhưng sự khoan dung này có giới hạn và vấn đề nghiêm trọng vẫn lộ ra.
  - Với designer, đây là cái bẫy: vẻ đẹp che vấn đề khỏi người đánh giá.
  - Trong usability test, người tham gia vật lộn với một task rồi khen giao diện, và lỗi thật không bao giờ được gọi tên.
  - Hai biểu đồ trên slide chỉ minh hoạ chiều của kết quả, không phải dữ liệu gốc của nghiên cứu.
  > Lần gần nhất bạn khen một thiết kế đẹp, bạn đã thử dùng nó chưa?
- Ví dụ: có (nghiên cứu Kurosu và Kashimura 1995, trong lesson)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Two scatter plots on shared axes, drawn plainly. "Appeal vs perceived usability" steep and tight, `--sienna`. "Appeal vs actual usability" shallow and scattered, `--ink-muted`. Both are illustrative of the direction of the finding, not the study's data: label each "illustrative" in `--font-mono`. No chart junk, no gridlines beyond the axes.

---

### DIAGRAM · The floor rose
- Kicker: Why this matters now
- Title: Attractiveness is no longer *scarce.*
- On-slide: A signal only works while it separates the options. Looking fine no longer does.
- Speaker notes:
  - Các công cụ tạo sinh nâng mặt bằng thẩm mỹ lên cho mọi người, nên gần như mọi thứ bây giờ đều trông ổn.
  - Chỉ cần trông ổn thì không còn đủ để phân biệt các lựa chọn.
  > Một designer chỉ có gu làm công cụ đánh giá đã lặng lẽ mất công cụ đánh giá duy nhất của mình.
  - Concept bạn chọn lúc đầu cũng thuộc vùng “trông ổn”, nên nó qua được chỉ bằng cảm giác.
  - Nếu concept đó do AI vẽ thì tiêu chí vẫn như vậy.
  > Nguồn gốc không quan trọng. Tiêu chí giống nhau ở cả hai.
- Ví dụ: Không cần. Nhắc lại concept của mentee.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: A distribution curve of "visual quality" shown twice: a wide, low old curve in `--ink-muted`, and a compressed curve piled against the ceiling in `--sienna`. Nothing beneath the curves.

---

## 8. Layer 5 · Components

---

### SECTION DIVIDER · Layer 5
- Kicker: Layer 05
- Title: COMPONENTS
- On-slide: Why does this thing exist, and when should I not use it?
- Speaker notes:
  - Layer nặng nhất và gần nhất với nỗi bực hằng ngày của bạn.
  - Layer này dễ chạy quá giờ nhất và đáng để chạy quá.
  - Đây là layer duy nhất có yếu tố chính trị, vì bạn đang học cách đánh giá công việc của quản lý.
- Ví dụ: Không cần. Slide chia phần.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Five-plane locator, plane 5 in `--sienna`.

---

### COMPARE · Jakob's Law
- Kicker: Familiarity
- Title: Familiar beats *novel.*
- On-slide: LEFT a conventional control. RIGHT a novel one doing the same job
- Speaker notes:
  - Người dùng dành phần lớn thời gian ở các sản phẩm khác và muốn sản phẩm của bạn chạy giống những cái họ đã biết.
  - Một component lạ khiến người dùng tốn thời gian học, và chi phí đó cần một lợi ích bạn gọi tên được.
  > Bên phải mua được gì?
  - Thường là không có gì mà designer diễn đạt được.
  - Luật này không phản đối sáng tạo mà đòi hỏi khả năng biện minh cho nó.
  > Component nào trong concept của bạn khác thói quen người dùng, và bạn gọi tên được lợi ích của nó chưa?
- Ví dụ: bản nháp (một designer tự vẽ bộ chọn ngày dạng vòng tròn cho form đặt lịch trong khi cả team và người dùng đã quen lịch dạng lưới)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC, matched frames, same task in each. LEFT a standard control drawn from the kit. RIGHT the same function as an invented control. Neither marked. Let the mentee work out which one they'd rather hand to a user.

---

### DIAGRAM · A component is inherited reasoning
- Kicker: What's baked in
- Title: Inherited *reasoning.*
- On-slide: Default · hover · focus · active · disabled · loading · error · empty
- Speaker notes:
  > Dùng hệ thống không phải là ràng buộc với sáng tạo. Đó là tái sử dụng suy nghĩ.
  - Khi hiểu điều này, bạn không còn coi design system là một cái lồng, và chuyển biến đó đáng giá cả layer.
  - State là thứ junior hay bỏ qua.
  > Component chỉ được định nghĩa ở trạng thái default là một bức tranh, không phải một component.
  - State bị thiếu trở thành chỗ để developer tự ứng biến, nghĩa là designer đã ngừng đưa ra quyết định giữa chừng.
  - Một nút từ thư viện công khai thường có khoảng ba trong tám state ở bản thiết kế đầu.
  > Component của bạn có bao nhiêu trong tám state?
- Ví dụ: bản nháp (một file Figma chỉ có nút ở state default và hover, và developer tự quyết định disabled và loading)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC. One button exploded into its eight states in a grid, each labelled in mono. Default drawn solid. The other seven drawn in `--sienna` hairline outline only, so what's usually missing is literally an outline waiting to be filled.

---

### DIAGRAM · Tesler's Law
- Kicker: The best law for this conversation
- Title: Complexity only *moves.*
- On-slide: Either the user absorbs it, or the system does.
- Speaker notes:
  - Đây là luật hữu ích nhất của buổi cho các cuộc trao đổi với developer và BA.
  - Nó biến một cuộc tranh luận về gu thành một câu hỏi phân bổ.
  - "Mình nghĩ cái này nên đơn giản hơn" mời người nghe phản đối.
  > "Độ phức tạp này phải nằm ở đâu đó, và hiện giờ nó nằm ở người dùng. Có thể để nó nằm ở phía mình không?"
  - Kỹ sư dễ đồng ý với cách đặt thứ hai vì họ vốn đã nghĩ theo cách đó.
  > Độ phức tạp trên màn hình của bạn đang nằm ở ai?
- Ví dụ: bản nháp (form đăng ký bắt người dùng tự nhập mã vùng, trong khi hệ thống có thể suy ra từ số điện thoại)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC. A single mass on a beam between two labelled ends, "user" and "system". Shown twice: mass at the user end, mass at the system end. Identical mass in both, `--ink` fill. The beam tilts; the mass never shrinks.

---

### DIAGRAM · The hard case
- Kicker: What if it's actually bad?
- Title: Your confusion is *data.*
- On-slide: TWO POSSIBILITIES: **The component is well-reasoned** and you haven't learned to read it · **The component is sloppy** and your confusion is accurate. ONE TEST: run the five layers on the component itself.
- Speaker notes:
  - Component thường tệ thật, và nên nói thẳng điều đó thay vì giả vờ hệ thống luôn đúng.
  - Đây lại là Gulf of Evaluation, ở một bậc cao hơn: bạn không đánh giá được màn hình và cũng không đánh giá được hệ thống tạo ra nó.
  - Đáp án không phải "tin hệ thống" và cũng không phải "chỉ trích hệ thống".
  - Chạy năm layer lên chính component: spacing bên trong có nằm trên thang không, có một primary rõ không, chữ có lấy từ cùng thang không, vai trò màu và contrast có giữ ở mọi state không, mọi state có được định nghĩa không.
  - Nếu các quyết định hợp lý thì khoảng cách nằm ở bạn và đó là vấn đề học, một tin tốt.
  - Nếu hai quyết định không hợp lý thì khoảng cách nằm ở component, và bạn có ngôn ngữ cụ thể thay cho một cảm giác mơ hồ.
  > Đây là bề mặt thứ ba hôm nay: màn hình bạn không làm ra, concept bạn vẽ, và thư viện component nằm bên dưới cả hai. Vẫn là một công cụ.
- Ví dụ: bản nháp (một designer thấy dropdown của thư viện công khai khó hiểu, chạy năm layer và thấy disabled state không đạt contrast)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC. The five-plane stack rotated ninety degrees and aimed at a single component instead of a screen, so the instrument is visibly being reused. Two of the five planes flagged in `--sienna` with mono labels reading "doesn't resolve". The other three plain.

---

### STATEMENT · The guardrail
- Kicker: Say this out loud
- Title: Ask.\n*Don't indict.*
- On-slide: > *"I ran our button against these five checks and the internal spacing and the disabled state don't resolve for me. Can you walk me through the reasoning?"*
- Speaker notes:
  > Hỏi, đừng kết tội.
  > "Mình chạy button của team qua năm check này, spacing bên trong và disabled state chưa hợp lý với mình. Anh chị giải thích giúp mình lý do được không?"
  - Câu hỏi này khiến một junior trông cẩn thận.
  - Cùng một quan sát, nếu nói thành "design system của mình hỏng", sẽ khiến họ trông như một vấn đề, và điều đó được nhớ lâu hơn việc họ đúng hay sai.
  > Một junior đúng nhưng không còn ai muốn làm việc cùng thì chưa thắng gì.
- Ví dụ: Không cần. Ví dụ nằm trong chính câu mẫu.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Two speech bubbles using the deck's series bubble shape. The question in `--sienna`, open and generously sized. The accusation in `--ink-ghost`, smaller and tighter. Same words are not used in both; the contrast is in the framing, not the volume.

---

### STATEMENT · Dev sentence 05
- Kicker: Say this
- Title: *"Our button already handles\ndisabled and loading. If I make\na new one, we maintain two\nof them forever."*
- On-slide: all five sentences, stacked small beneath
- Speaker notes:
  > "Button hiện có đã xử lý disabled và loading. Nếu mình làm cái mới, team phải bảo trì hai cái mãi mãi."
  - Câu này kết bằng chi phí, thứ ngôn ngữ mà người nghe vốn đã quen suy nghĩ.
  > Trong cả năm câu, không câu nào có chữ "trông".
- Ví dụ: có (câu nói với developer của Layer 5, trong lesson)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: The fifth series bubble, filled. Beneath it the four earlier bubbles shown small and complete, so the set reads as a finished collection. This is the payoff for repeating the same bubble all session.

---

## 9. Close

---

### DIAGRAM · The screen, all five layers
- Kicker: What we did to it
- Title: One screen.\n*Five decisions.*
- On-slide: The tracking screen in six states, left to right: original, then after each layer
- Speaker notes:
  - Đây là phần thưởng của việc mang một màn hình suốt buổi.
  > Bước nào tạo khác biệt lớn nhất?
  - Câu trả lời khác nhau và cái nào cũng đáng nghe.
  - Sửa spacing trước làm lộ vấn đề hierarchy, nên các layer chạy theo thứ tự đọc, và bạn vừa thấy điều đó xảy ra thay vì được kể.
  - Không có phần tử, chữ hay ảnh nào được thêm vào.
- Ví dụ: có (màn hình theo dõi đơn hàng qua sáu trạng thái, trong lesson)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: REAL. Six thumbnails of the same screen in a row, each labelled in mono with the layer just applied. The progression must be legible at a glance from across a table. This is the deck's closing image and worth building carefully.

---

### TWO-COLUMN · Two outputs
- Kicker: What you take away
- Title: What you did, and *why.*
- On-slide: LEFT **Decision sheet** what changed · which layer · which rule · the sentence you'd say to a dev. RIGHT **Token set** spacing scale · type scale · colour roles · what's still undefined
- Speaker notes:
  - Concept đã chọn chưa phải phần quan trọng nhất, vì ai cũng cho xem được một concept.
  - Chỉ có lý do mới tranh luận được hiệu quả.
  - Token set không phải một bảng màu tự nghĩ ra mà là hệ thống ngầm mà concept đã chọn đang dùng, được viết xuống.
  > Người viết hệ thống ngầm ra thành văn bản trở nên hữu ích hơn nhiều so với công sức họ bỏ ra.
  - Token set là đầu vào cho nhiệm vụ 1 của buổi Figma, nơi chúng trở thành variables, và sau đó giúp công cụ tạo sinh không tự bịa ra một hệ thống riêng ở mỗi màn hình.
  - Decision sheet là đầu vào cho critique, nơi câu hỏi chuyển từ "bạn có thích không" sang "lý do được nêu có đứng vững không".
- Ví dụ: có (hai output của lesson)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Two document specimens side by side, drawn in the schematic kit as filled-in sheets rather than blank ones. Arrows from each pointing right to a labelled destination.

---

### STATEMENT · The one thing
- Kicker: Carry this out
- Title: You'll spend most of your\ncareer judging work\n*you didn't make.*
- On-slide: The five layers are not a checklist for making screens. They're how you form an opinion you can defend.
- Speaker notes:
  > Bạn sẽ dành phần lớn sự nghiệp để đánh giá công việc bạn không làm ra.
  - Đến đây, phụ đề ở trang bìa mới có đủ nghĩa.
  - Mọi bề mặt hôm nay đều có nguồn từ trước: màn hình bạn không làm, concept bạn vẽ từ process map, component của người khác.
  - Không thứ nào trong buổi này được tạo từ trang trắng, và đó là điều kiện thật của công việc.
  > Bảo vệ được một ý kiến là năng lực hiếm hơn mức đáng ra phải có.
- Ví dụ: Không cần. Slide kết, không giới thiệu khái niệm mới.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: SCHEMATIC. The three surfaces from the session as three small specimens (a grid of screens, one screen, one component), all three feeding into the five-plane instrument in `--sienna`. The instrument is the constant; the surfaces change.

---

## 10. Practice and homework

---

### MILESTONE · Practice
- Kicker: Practice
- Num: 16 min
- Title: Choose between\n*your* concepts
- Prompt: Run the five layers on each concept. Fill one row per layer. Pick one and say why the others lost.
- On-slide: nothing else
- Speaker notes:
  > Chọn một concept bằng cảm giác trước và nói lý do trong một câu.
  - Practice chạy trên hai hoặc ba concept bạn vẽ cho một bước trong process map, không chạy trên màn hình giao đồ ăn. Màn hình giao đồ ăn là bề mặt để dạy, còn flow của bạn là bề mặt để thực hành.
  - Chạy năm layer lên từng concept theo thứ tự, dừng ở layer đầu tiên không ổn, và điền decision sheet với mỗi layer một dòng.
  - Layer 1 và 2 được đối chiếu với process map: gì thuộc cùng nhau ở bước này, và hành động chính duy nhất là gì.
  - Mỗi dòng của decision sheet gồm quyết định, layer, luật và câu nói với developer.
  - Sau khi chọn một concept, mỗi concept còn lại cần một dòng giải thích vì sao thua theo layer chứ không theo gu.
  - Ở phần share-back, mình đóng vai developer và hỏi "says who?" cho từng dòng cho đến khi lý do đứng được mà không cần chữ "trông".
  - Token set được hoàn thành ở bài tập về nhà.
  - Blur và desaturate áp dụng được lên concept của bạn trong vài giây.
- Ví dụ: có (practice của lesson: chọn giữa các concept của chính mình)
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Full-bleed milestone treatment. Large "16 min", title, prompt. No diagram.

---

### DIAGRAM · Homework
- Kicker: After the session
- Title: Homework
- On-slide: **01 · Decision sheet** · **02 · Clean concept** · **03 · Token set** · **04 · Component question**
- Speaker notes:
  > Phần việc còn lại của buổi này là bài tập về nhà, và cả hai output đều là đầu vào cho buổi Figma.
  - Hoàn thiện decision sheet: mỗi layer một dòng, với lý do chịu được câu hỏi "says who?".
  - Tinh chỉnh concept đã chọn thành một màn hình sạch ở trạng thái default, chỉ sửa layer đầu tiên không ổn.
  - Viết token set từ concept đó: spacing trên thang 8, tối đa ba cỡ chữ và hai weight, mỗi màu một role, và ít nhất một thứ chưa được định nghĩa.
  - Chạy năm layer lên một component của thư viện công khai và viết một câu hỏi cho team theo kiểu hỏi, không kết tội.
  - Bước nhờ AI đánh giá concept là tuỳ chọn, và một nhận định về contrast của AI cần được kiểm tra lại bằng công cụ đo.
  > Câu nào trong decision sheet của bạn còn dùng chữ "trông"?
- Ví dụ: Không cần. Tóm lại các bước của lesson.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Four numbered cards in a row (Design System Card Row), the token set card emphasised in `--ink` fill with the number in `--yellow`. No specimen.

---

## 11. End

---

### END
- Title: UI Fundamentals
- Subtitle: Judging design decisions you didn't make.
- On-slide: Winnie Nguyen · 2026
- Speaker notes:
  - None.
- Ví dụ: Không cần. Slide kết thúc.
- Câu hỏi hay gặp: None.
- 🎨 Visual hint: Same visual language as the cover, quieter. The tracking screen now shown in its corrected state, small.
