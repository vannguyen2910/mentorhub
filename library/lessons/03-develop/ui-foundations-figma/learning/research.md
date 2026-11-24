# UI Foundations: Building in Figma — desk research

*Ngày: 2026-10-31. Giai đoạn research: chưa viết lesson, chưa có brief. Mục đích: gom nguồn trong repo, Notion và web cho các learning objectives, đánh dấu nguồn nào chính thức, nguồn nào chỉ là blog.*

## 1. Bối cảnh đã chốt với Winnie

- Buổi 90 phút, trong đó khoảng 10 phút đầu xem file của mentee, còn khoảng 80 phút để dựng.
- Mentee làm ngay từ đầu, trên file của chính họ. Không có phần demo trước.
- Winnie chỉ ra chỗ sai và sửa cùng mentee ngay lúc làm.
- Giữ grid, 8pt, typography, color ở buổi này nhưng ngắn, chỉ đủ để dựng variables và component. Phần phán đoán visual để buổi UI Fundamentals.
- Không có AI trong buổi này.
- Lesson viết generic, không nhắc tên mentee.

Learning objectives (từ coaching plan):
1. Tổ chức file Figma để ai cũng tìm được đường
2. Dùng auto layout và variables để dựng layout linh hoạt
3. Tạo component và variants từ màn hình của chính mình
4. Điều chỉnh layout qua các breakpoint

## 2. Trong repo và Notion

| Nguồn | Dùng được gì | Lưu ý |
|---|---|---|
| `library/lessons/03-develop/design-system/materials/design-system-lesson.md` (mục "Atomic Design in Figma") | Tokens là Variables, component variants, quy tắc đặt tên `a/m/o`, 8pt grid | Bản nháp; trùng một phần với buổi này, cần chia ranh giới với buổi Design System |
| `library/_recovered-2026-10-02/.../ui-fundamentals-lesson.md` | 5 layer (space, hierarchy, type, colour, component) | Bản khôi phục, README ghi nhầm là đã ở `03-develop/`. Đây là buổi sau, không dạy lại ở đây |
| Notion "Overview & Learner Profile" của mentee | Gap ưu tiên số 1: Figma craft (auto layout, variables, components, file sạch) | Trang riêng của coach, không đưa nội dung cá nhân vào lesson |
| Notion "Day 1: Learn Figma" (2019), "UI/UX Class" (2023) | Ghi chú cũ của Winnie | Chưa đọc kỹ, cần mở nếu muốn tái dùng |

## 3. Nguồn ngoài

Nguồn chính thức dùng được để nêu như sự thật. Blog chỉ dùng làm gợi ý và phải nói rõ là ý kiến.

### Chính thức

| Chủ đề | Nguồn | Điều nguồn nói |
|---|---|---|
| Variables, collections, modes, alias | [Create and manage variables and collections](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables-and-collections), [Modes for variables](https://help.figma.com/hc/en-us/articles/15343816063383-Modes-for-variables) (Figma Help) | Tạo collection, tạo variable, alias bằng "Create alias", mỗi collection có mode riêng, số mode phụ thuộc gói |
| Auto layout, Hug / Fill / Fixed, min và max | [Figma Help: Guide to auto layout](https://help.figma.com/hc/articles/360040451373) | Hug theo nội dung con; Fill chỉ áp cho con của auto layout; gõ số vào width sẽ chuyển sang Fixed; min và max dùng được cùng các chế độ khác |
| Component properties | [Explore component properties](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties), [Create and manage component properties](https://help.figma.com/hc/en-us/articles/8883756012823-Create-and-manage-component-properties) (Figma Help) | Bốn loại: boolean, instance swap, text, variant. Boolean chỉ điều khiển ẩn hiện layer. Variant property chỉ tạo từ component set cha |
| Breakpoint | [Material Design 3: Breakpoints](https://m3.material.io/foundations/layout/applying-layout), [Android Developers: window size classes](https://developer.android.com/develop/ui/views/layout/use-window-size-classes) | Compact dưới 600dp, medium 600 đến 839dp, expanded 840 đến 1199dp, large 1200 đến 1599dp, extra-large từ 1600dp. Compact và medium nên một pane, expanded và large nên hai pane |
| Contrast màu | [WCAG 2.2 Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) (W3C) | 4.5:1 cho chữ thường, 3:1 cho chữ lớn (từ 18pt, hoặc 14pt đậm); so sánh không làm tròn nên 4.499:1 là trượt |
| Design tokens | [Design Tokens Format Module 2025.10](https://tr.designtokens.org/format/) (Design Tokens Community Group) | Bản ổn định đầu tiên, 2025-10-28. Mỗi token có type và value theo type đó. Mới đọc qua đoạn trích, chưa đọc toàn văn |

### Blog và ý kiến (dùng thận trọng)

| Chủ đề | Nguồn | Điều nguồn nói |
|---|---|---|
| Tách primitive và semantic | [Red Hat UX: Figma variables and styles](https://ux.redhat.com/get-started/designers/figma-variables-and-styles), [Using design tokens as variables](https://designtokens.substack.com/p/using-design-tokens-as-variables) | Component dùng semantic, không dùng primitive trực tiếp. Red Hat nói chặt hơn các nguồn khác: không dùng primitive trừ khi bắt buộc. Đây là lựa chọn của từng team |
| Tên variable dạng đường dẫn | cùng hai nguồn trên | Ví dụ `typography/heading/h1/font-size` |
| Tổ chức file | [designproject.io](https://designproject.io/blog/how-to-organize-figma-files/), [Design Shack](https://designshack.net/articles/business-articles/figma-team-collaboration) | Một quy ước đặt tên nhất quán; tách page nháp, page duyệt, page handoff; dùng section; một page ghi chú quy tắc. Không phải chuẩn |
| 8pt grid | [ls.graphics](https://www.ls.graphics/blog/why-8pt-grid-the-math-behind-clean-ui), [Queensland Government Design System: spacing](https://www.designsystem.qld.gov.au/styles/spacing/design) | Thang 4, 8, 16, 24, 32, 48, 64, 96; số nguyên ở 1x, 2x, 3x. Nhiều nguồn khuyên lai: 4pt cho chi tiết nhỏ, 8pt cho phần còn lại. Cỡ chữ theo thang riêng, không theo 8pt. Chưa đối chiếu tài liệu gốc của Material hay Carbon |

## 4. Chỗ chưa chắc

- Bài viết cộng đồng nói alias giữa collection chỉ lấy giá trị, không chọn được mode. Bài đã cũ (khoảng 3 năm) và chưa có nguồn mới xác nhận. **Phải thử trong Figma trước khi dạy.**
- Một tutorial bên thứ ba nói Fixed width bỏ qua min và max. Tài liệu chính thức của Figma không nói vậy. Không dùng.
- Số mode tối đa phụ thuộc gói Figma của mentee; cần hỏi trước buổi học.
- Chưa tìm nguồn có số liệu về tỷ lệ designer dùng hay không dùng auto layout hoặc variables. Không nêu con số nào trong lesson trừ khi có nguồn.
- Phương pháp "nền tảng ngắn rồi dựng variables" là cách dạy của Winnie, không có nghiên cứu nào đi kèm.

## 5. Còn mở (cần Winnie quyết trước brief)

1. Với 80 phút, bỏ hoặc chuyển thành homework nhiệm vụ nào trong năm nhiệm vụ: dọn file, variables, auto layout, component và variants, breakpoints.
2. Ranh giới với buổi Design System: buổi này dừng ở variables cộng một vài component, hay đi đến cả quy tắc đặt tên `a/m/o`?
3. Guide gửi trước buổi (dọn file) có nằm trong phạm vi lesson này không.

---

# Cập nhật 2026-11-24: nên dạy gì, lỗi thường gặp, yêu cầu việc làm, hình ảnh

*Cách làm: 5 subagent haiku thu thập song song (tính năng Figma, giáo trình, lỗi thường gặp, JD, danh mục ảnh), thêm một lượt kiểm tra lại 4 trang chính thức. Các trang đọc qua công cụ fetch rồi được model nhỏ tóm tắt, chưa mở trong trình duyệt, nên nhãn giao diện và giới hạn gói vẫn phải thử trong app trước khi dạy. Phần này chỉ là research, chưa sửa brief hay lesson.*

## A. Kết luận ngắn

1. **File organization là khoảng trống lớn nhất của các khoá học.** Trong 12 tài liệu so sánh, gần như không khoá nào dạy riêng việc này. JD cũng nhắc gián tiếp (2/12 JD đọc trực tiếp, ví dụ "file gọn, scalable"). Giữ phần kiểm file ở đầu buổi và guide gửi trước là hợp lý.
2. **Auto layout và component là thứ thị trường đòi nhiều nhất.** Component, design system xuất hiện ở 9/12 JD, auto layout ở 4/12. Cả hai đều có nhiều lỗi lặp lại, có thể dùng làm ví dụ sai và đúng.
3. **Variables: JD ít nhắc (3/12, toàn Việt Nam, 0/5 quốc tế), nhưng brief đang dành 22 phút đầu cho phần này.** Mẫu rất nhỏ nên chưa đủ để đổi thứ tự. Lý do giữ variables trước vẫn nằm ở sư phạm: component dùng token ngay từ đầu thì không phải sửa lại. Đây là quyết định của Winnie (xem mục F).
4. **Breakpoint: 0/12 JD nhắc, và không giáo trình nào gọi tên nó như một tính năng.** Figma không có media query ở design mode, người ta làm bằng min/max width, variable mode và frame nhân bản. Brief đã cho phép rút Nhiệm vụ 4 xuống một component và một màn hình; research ủng hộ việc coi đây là phần co giãn được.
5. **Thứ tự dạy trong brief (variables, auto layout, component, breakpoint) khớp với khoá có cấu trúc gần nhất** (Frontend Masters, Figma for Developers v2): layout, rồi variables, rồi component, rồi responsive bằng modes. Các khoá khác thường dạy auto layout trước và variables sau; không có thứ tự nào là chuẩn.
6. **Có hai thay đổi 2026 của Figma ảnh hưởng thẳng đến Nhiệm vụ 2 và 3** (mục B). Cần mở file thật trước khi dạy.

## B. Tính năng Figma hiện tại (cần kiểm trong app)

| Chủ đề | Điều đã đọc được | Nguồn | Mức chắc |
|---|---|---|---|
| Auto layout, hai phiên bản | Bản "updated" là mặc định cho frame mới từ tháng 7/2026. Chuyển qua lại được đến tháng 1/2027, sau đó frame cũ chỉ còn nút Update. Component không tự nâng cấp | [help 42031586813719](https://help.figma.com/hc/articles/42031586813719) | Đã kiểm lại, trang không ghi ngày |
| Auto layout, mô tả | "Gần CSS hơn", mã Dev Mode khớp flexbox hơn | [forum.figma.com, 2026-07-24](https://forum.figma.com/product-updates-3/design-closer-to-css-with-the-updated-auto-layout-option-56357) | Bài của Community Support |
| Padding đặt kích thước tối thiểu | Padding 30px mỗi bên thì frame không hẹp hơn 60px, max width không ghi đè | cùng bài help | Chưa kiểm lại |
| Hug, Fill, Fixed, min/max trong frame thường | Trang help chưa nói rõ áp dụng cho frame thường hay chỉ Figma Sites | cùng bài help | **Chưa xác nhận.** Phải thử trong app |
| Variable modes | Professional tối đa 10 mode mỗi collection, Organization 20, Enterprise không giới hạn | [blog Schema 2025, 2025-10-28](https://www.figma.com/blog/schema-2025-design-systems-recap/), [bảng gói](https://help.figma.com/hc/en-us/articles/360040328273) | Đã kiểm lại |
| Gói Starter | Bảng gói để trống ở dòng variable modes và Dev Mode. Trang "Guide to variables" lại nói variables dùng được trên các gói | hai trang trên | **Mâu thuẫn, chưa phân xử.** Thử trên một file Starter thật |
| Tên panel Variables, đường mở | Không trang nào ghi rõ | [Guide to variables](https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma) | Chưa có. Ghi từ app |
| Loại component property | Năm loại: Boolean, Instance swap, Text, Variant, Slot. Simplified instances bị bỏ từ 2026-03-23 | [help Variants](https://help.figma.com/hc/en-us/articles/5579474826519-Variants) | Chưa kiểm lại |
| Giới hạn Starter | Một team, một folder, ba file | [bảng gói](https://help.figma.com/hc/en-us/articles/360040328273) | Chưa kiểm lại. Quan trọng nếu học viên làm trong file riêng |

Hệ quả khi dạy:
- Trước buổi, kiểm tra file của học viên đang ở auto layout bản cũ hay bản mới, vì lỗi Hug và Fill và cách panel hiện min/max có thể khác nhau.
- Nếu học viên dùng gói Starter, thử trước xem tạo được collection và thêm mode không. Nếu không, Nhiệm vụ 1 cần một file mẫu hoặc bản chụp từ gói Professional.
- Không đưa số mode, giá hay nhãn menu cụ thể vào slide khi chưa tự kiểm trong app. Giá (Professional Full seat 16 USD mỗi tháng, ghi nhận 2026-11-24) đổi thường xuyên, không nên đưa vào.
- Figma Make và các tính năng AI trong Figma có trong release notes 2026, nhưng chỉ 1/12 JD nhắc. Giữ ngoài buổi này, đúng quyết định "không có AI" trong brief.

## C. Người khác dạy gì (12 tài liệu)

Chi tiết từng khoá nằm trong báo cáo thô; các điểm rút ra:

- **Khung gần nhất:** [Figma for Developers v2, Frontend Masters](https://master.dev/courses/figma-v2), 4 giờ 12 phút, 20 demo và 8 bài tập (ngày 2024-06-04). Thứ tự: giao diện, layout và auto layout, styles và variables, component, responsive bằng modes.
- **Thường dạy trước:** tour giao diện, layers, auto layout cơ bản. Component luôn đứng trước variant.
- **Ít được dạy, hoặc chỉ nhắc:** file organization (chỉ có đôi bài về layers, frames, sections), breakpoint như một khái niệm riêng (chỉ Skillshare Responsive Deep Dive của Christine Vallaure, chưa kiểm được trang), variants.
- **Không thống nhất:** variables trước hay sau component; constraints trước hay sau auto layout; responsive bằng grid và constraints, bằng modes, hay mobile-first; demo trước hay làm ngay.
- Cách dạy "làm ngay không demo" của Winnie giống Packt và Google UX; Frontend Masters và LinkedIn demo trước. Chưa có nguồn nào so sánh hiệu quả của hai cách.
- **Chưa kiểm được:** hai khoá Skillshare (403), thời lượng khoá Google UX (hai nguồn lệch: 2 tuần x 10 giờ so với khoảng 19 giờ), Interaction Design Foundation (không thấy khoá Figma), Maven (404), kênh YouTube của Figma.

## D. Lỗi thường gặp (39 mục, chọn 16 mục đáng đưa vào buổi học)

Đếm "số nguồn" là đếm tay trên khoảng 20 truy vấn, chỉ dùng để so sánh tương đối. Reddit không truy cập được, nguồn chính là forum.figma.com, help.figma.com và blog. Nhiều thread cũ nên chỉ dùng để giải thích vì sao người ta hay nhầm.

| Nhiệm vụ | Lỗi | Nguồn tốt nhất |
|---|---|---|
| Auto layout | Cha để Hug, con để Fill: cha không co được, con tự đổi sang Fixed (4 nguồn) | [help auto layout](https://help.figma.com/hc/en-us/articles/360040451373) |
| Auto layout | Không thấy Fill vì cha không phải auto layout hoặc con đang absolute position (3) | [forum](https://forum.figma.com/t/why-is-there-no-fill-container-option-when-selecting-child-elements/58344) |
| Auto layout | Kéo tay một layer cho khít thì nó thành Fixed (2) | help auto layout |
| Auto layout | Không biết có min/max trong dropdown Width, nên đặt kích thước cứng hoặc dùng layer trong suốt giữ chiều rộng (3 + 2) | help auto layout |
| Variables | Đã có variable nhưng vẫn dán hex cứng (2) | [Check designs](https://help.figma.com/hc/en-us/articles/39592284074263-Check-designs-in-Figma) |
| Variables | Dùng primitive thẳng trong component, bỏ qua lớp semantic (3) | [Figma, design tokens](https://www.figma.com/resource-library/design-tokens/) |
| Variables | Đặt tên theo màu ("Blue") thay vì theo vai trò (3) | [forum](https://forum.figma.com/ask-the-community-7/about-naming-colors-in-design-systems-beginner-in-figma-39743) |
| Variables | Nhầm collection, mode, variable; tạo quá nhiều collection (3) | [Guide to variables](https://help.figma.com/hc/en-us/articles/15145852043927-Guide-to-variables-in-Figma) |
| Variables | Mode áp theo frame, các lớp lồng nhau có thể giữ mode khác; text style không theo mode (3 + 3) | [forum](https://forum.figma.com/t/modes-getting-mixed-up-and-showing-other-mode-variables-when-switching-between-the-two/91635) |
| Component | Detach instance để sửa nhanh, mất cập nhật hàng loạt (2) | [Salesforce, component health](https://www.salesforce.com/blog/figma-component-health/) |
| Component | Override mất khi publish hoặc khi đổi variant của cha (3 + 3) | [forum](https://forum.figma.com/archive-21/modifying-component-resets-overrides-on-instances-of-that-component-24126) |
| Component | Định nghĩa property sau khi đã tạo variant, phải làm lại (2) | [forum](https://forum.figma.com/t/cant-delete-a-property-from-a-component/68633) |
| Component | Đặt tên variant Yes/No, bị đổi thành boolean (2) | [forum](https://forum.figma.com/t/no-yes-variants-after-being-automatically-converted-to-boolean-are-still-treated-as-string-stopping-boolean-variables-binded-to-an-instance-from-working/65661) |
| File | Tên layer mặc định, dùng group thay frame (3 + 3) | [Figma, groups versus frames](https://www.figma.com/best-practices/groups-versus-frames/) |
| File | Một trang chứa tất cả, không có trang chốt cho handoff (3 + 2) | [Viget](https://www.viget.com/articles/figma-tips-for-non-designers-part-1-structure-ui-basics) |
| Breakpoint | Nhân bản frame desktop sang mobile rồi sửa từng bản; tìm nút "breakpoint" không thấy (2 + 2) | [Medium, variables và breakpoints](https://medium.com/design-bootcamp/using-variables-to-work-with-breakpoints-in-a-responsive-way-on-figma-a6001d397a09) |

**Tám dấu hiệu "file xấu" để làm bài tập sửa file:** (1) tên layer mặc định như Frame 123; (2) hex cứng, không gắn variable; (3) instance đã detach; (4) Button, Button 2, Button copy thay cho variant; (5) group dùng làm bố cục; (6) cha Hug, con Fill; (7) kích thước Fixed khắp nơi, không có min/max; (8) một trang lộn xộn lẫn nháp và bản cuối. Tám dấu hiệu này phủ gần đủ các nhiệm vụ của buổi và có thể dựng thành một file mẫu xấu để học viên sửa.

Một ý đáng cân nhắc, chưa phải kết luận: Nhiệm vụ 1 và 2 có thể mở bằng một file mẫu xấu, học viên tìm lỗi trước khi sửa. Cách này khớp với câu hỏi mở số 3 trong brief về ví dụ lỗi thường gặp.

**Cần kiểm lại trước khi dạy:** thread cũ nói max width không làm được (nay có min/max trong dropdown Width); trang help về Fill container ghi cho Figma Sites, chưa rõ áp dụng cho frame thường; lỗi đổi hướng auto layout đặt lại về Hug chỉ thấy ở một bản desktop.

## E. Yêu cầu việc làm (mẫu nhỏ, không phải thống kê thị trường)

12 JD đọc trực tiếp (7 Việt Nam, 5 quốc tế) và 6 đoạn trích chưa mở được trang. Phần lớn JD đã đóng; ngày đăng từ 2025 đến 2026. LinkedIn, VietnamWorks, TopCV chi tiết và Wellfound không truy cập được. Nhiều tin ghi "junior" nhưng đòi 2 đến 4 năm kinh nghiệm.

| Chỉ số | Việt Nam (n=7) | Quốc tế (n=5) |
|---|---|---|
| Auto layout | 3 | 1 |
| Variables | 3 | 0 |
| Component, design system, library | 6 | 3 |
| Prototyping | 5 | 5 |
| Dev Mode, handoff | 4 | 1 |
| Responsive, breakpoint | 0 | 0 |
| Tổ chức file | 1 | 1 |
| Plugin | 0 | 0 |
| AI trong Figma | 0 (AI nói chung: 3) | 1 |

Nhóm 6 đoạn trích cho thấy auto layout và component xuất hiện nhiều hơn (3/3 ở cả hai thị trường), nhưng có thể thiên lệch vì tìm bằng từ khoá Figma, không nên dùng làm số liệu chính.

Khảo sát: [Figma, State of the Designer 2026](https://www.figma.com/reports/state-of-the-designer-2026/) nằm sau form nên chưa đọc được. [ITJobsWatch](https://www.itjobswatch.co.uk/jobs/england/figma.do) (Anh, đến 2026-01-01) cho thấy nhu cầu Figma tăng nhẹ. Không tìm được khảo sát công khai nào riêng về kỹ năng Figma của junior. Không trích con số phần trăm nào từ nguồn thứ cấp vào lesson.

## F. Điều cần Winnie quyết định

1. **Đã chốt 2026-11-24: giữ variables ở Nhiệm vụ 1 nhưng thu gọn, không đảo xuống sau auto layout.** *Chưa áp vào brief.*
   - Lý do giữ trước: Nhiệm vụ 2 gắn padding và gap vào variables nên cần variables có trước; token đã rút ra từ buổi UI Fundamentals nên chỉ chuyển giá trị thành variables; khớp Frontend Masters v2.
   - Lý do thu gọn: variables có trong 3/12 JD (mẫu nhỏ), lỗi hay gặp nằm ở khâu gắn và đặt tên chứ không ở khâu tạo, modes chỉ cần cho Nhiệm vụ 4 và chưa chắc dùng được trên gói Starter.
   - Nội dung đã chốt: Nhiệm vụ 1 còn khoảng 15 phút, hai collection (primitive và semantic), ba nhóm (spacing, vai trò màu, cỡ chữ), đặt tên theo vai trò, alias từ semantic về primitive, chưa dạy modes. Modes chuyển sang Nhiệm vụ 4; nếu Nhiệm vụ 4 bị rút thì modes đi theo, success check không đổi. Khoảng 7 phút dư chuyển sang Nhiệm vụ 2 và 3 (lỗi Hug và Fill, detach và override).
   - Phương án đã không chọn: auto layout và component trước, variables làm bước refactor sau cùng (dùng Check designs để tìm hex cứng).
   - Chưa thử với học viên thật. Khi áp vào brief, theo quy tắc: giữ bản cũ trong `materials/_archive/` với hậu tố `-pre-variables-order-YYYY-MM-DD`.
2. **Đã chốt 2026-11-24: Nhiệm vụ 4 (breakpoints và modes, 14 phút) giữ là phần chính.** Brief đã đổi: khi quá giờ thì rút Nhiệm vụ 3 xuống hai component, không cắt Nhiệm vụ 4. Research ban đầu nghiêng về coi đây là phần mở rộng (0/12 JD nhắc breakpoint); quyết định này theo ý Winnie.
3. **Đã chốt 2026-11-24: tạo file mẫu "xấu" làm bài tập sửa ở Nhiệm vụ 1 và 2.** Còn mở: cách xếp vào 15 và 21 phút, và quan hệ với "làm ngay trên file của mình, không demo".
4. **Đã chốt 2026-11-24: học viên dùng gói Pro.** Modes dùng được (tối đa 10 mỗi collection), không cần phương án Starter.
5. **Kiểm trong app:** Winnie không có thời gian tự thử; kiểm bằng Figma MCP (kết quả ghi ở mục I nếu làm được). Lưu ý tài khoản của Winnie đều là gói Starter, nên kết quả về modes trên Pro không thử được.

## G. Hình ảnh

Kết quả danh mục ảnh có giấy phép mở: **rất ít.** Chỉ khoảng 4 mục có giấy phép mở, và đều là code hoặc token, không phải ảnh hay file Figma (repo token của Primer, MIT; code GOV.UK Frontend, MIT, tài liệu theo OGL 3.0; code Carbon, Apache 2.0). Chưa mở file LICENSE của các repo nên cần kiểm lại. Wikimedia Commons không có ảnh phù hợp. Figma Community cho duplicate file nhưng giấy phép khác nhau theo từng file, chưa xác nhận file nào là CC BY hay MIT. Các bộ kit Material 3, Carbon, Polaris, Red Hat, GOV.UK, Queensland chỉ nên xem bằng link, không dùng lại.

Đề xuất, chưa thực hiện:
- **Ảnh chụp giao diện Figma:** tự chụp trên file của Winnie, vì không có nguồn mở. Các màn hình cần chụp: panel Variables với collection primitive và semantic; Auto layout settings (bản cũ so với bản mới); dropdown Width có Add min width và Add max width; Properties của component set; layers panel của file xấu và file sạch.
- **Sơ đồ khái niệm, vẽ bằng diagram-design:** Hug, Fill, Fixed; min và max; chuỗi alias primitive sang semantic sang light và dark; component set với variant property và boolean; cây layer sạch và lộn xộn; ba frame theo breakpoint.
- **File ví dụ:** dựng một file xấu từ tám dấu hiệu ở mục D thay vì tìm file có sẵn.
- **Chưa tải ảnh nào.** Nếu muốn thử thêm, việc duyệt tay Figma Community (tìm "auto layout", "variables", "component properties") và Category:Responsive web design trên Wikimedia Commons cần đọc giấy phép từng file; sẽ xin duyệt từng file trước khi tải.

## H. Còn chưa chắc

- Giới hạn gói Starter với variables và modes (mâu thuẫn giữa hai trang help).
- Tên panel Variables và các nhãn giao diện khác.
- Hug, Fill, Fixed và min/max có áp dụng giống nhau ở bản auto layout cũ và mới, trong frame thường, hay không.
- Giáo trình Skillshare, Google UX, Interaction Design Foundation, Maven, kênh YouTube của Figma chưa kiểm được.
- Reddit, LinkedIn, VietnamWorks, TopCV chi tiết, Wellfound không truy cập được; số JD dưới mục tiêu và thiên lệch chọn mẫu.
- Cách dạy "làm ngay không demo" chưa có nguồn so sánh hiệu quả; vẫn là lựa chọn của Winnie.

## I. File mẫu xấu và thử nghiệm bằng Figma MCP (2026-11-24)

**File đã dựng:** [UI Foundations Figma - file mẫu xấu và thử nghiệm](https://www.figma.com/design/NqISsz8DBwokoJSfjE8SWO) (file nháp trong team Personal Workplace của Winnie, gói Starter). Ảnh chụp màn hình chính: `assets/bad-file-sample-screen.png`.

Nội dung: một màn hình "Lịch hẹn của tôi" kèm hai bản sao trên cùng một page (`Frame 1`, `Frame 1 copy`, `Frame 1 final 2`, một ghi chú "NHÁP"), một component `Button` không ai dùng và một bản `Button` đã detach. Đủ cả 8 dấu hiệu ở mục D:

| # | Dấu hiệu | Có trong file ở đâu |
|---|---|---|
| 1 | Tên layer mặc định | `Frame 1`, `Frame 2`, `Rectangle 3`, `Group 1`, `Text 5`... |
| 2 | Hex cứng | Mọi màu đều gõ tay; ba sắc cam gần giống nhau (`#E8590C`, `#E8590D`, `#e75a0c`) và nhiều xám gần giống (`#333333`, `#3A3A3A`, `#2f2f2f`) |
| 3 | Detached instance | `Button` đã detach, kèm component gốc bị bỏ không |
| 4 | Nút copy thay variant | `Button`, `Button 2`, `Button copy`, `Button final`; khác nhau về bo góc (8, 10, 12, 9) và padding |
| 5 | Group làm bố cục | `Group 1` ở header, các phần tử card đặt tay bằng x, y |
| 6 | Hug và Fill mâu thuẫn | Hàng "Nhắc tôi trước 30 phút": cha Hug, con Fill |
| 7 | Fixed khắp nơi | Card 350 x 158, ba hàng danh sách 350 x 64, không có min và max |
| 8 | Một page lẫn nháp và bản cuối | Chỉ có `Page 1`, ba màn hình và ghi chú nháp |

**Quan sát thật (không phải từ tài liệu):** khi dựng hàng Hug và Fill bằng Plugin API, Figma chấp nhận cấu hình này. Cha hug lại rộng 130 px, con Fill chỉ còn 100 px, và dòng chữ "Nhắc tôi trước 30 phút" bị cắt ở "Nhắc tôi trước 3" (xem ảnh). Đây là triệu chứng cụ thể để học viên nhìn thấy trước khi nghe giải thích. Cần xác nhận lại bằng thao tác tay trong giao diện, vì tôi dựng bằng API chứ không kéo chuột.

**Chưa làm được:** các thử nghiệm về modes và alias giữa collection, min và max trong frame thường, và phiên bản auto layout, vì Figma MCP trên gói Starter đã chạm giới hạn số lần gọi ("You've reached the Figma MCP tool call limit on the Starter plan"). Dừng ở đó, không tìm cách vượt giới hạn. Các điểm vẫn chưa xác nhận:
- Alias giữa collection có chọn được mode không (mục [to confirm] của brief).
- Min và max width có chạy trong frame thường không (help chỉ nói rõ cho Figma Sites).
- Auto layout bản "updated" so với bản cũ.
- Tên panel Variables và đường mở (Plugin API không trả về nhãn giao diện, nên cách nào cũng phải nhìn app).
- Gói Starter có thêm mode được không: không còn liên quan, vì học viên dùng gói Pro.

Thử lại khi giới hạn reset, hoặc khi Winnie nâng gói. Kịch bản thử đã sẵn: tạo hai collection, thêm mode, đặt alias, đặt explicit mode cho node và đọc giá trị resolve; rồi một frame auto layout có con Fill với min và max width, đổi kích thước cha và đọc kích thước con.

## J. Sơ đồ khái niệm đã vẽ (2026-11-24)

Sáu sơ đồ bằng diagram-design, skin mặc định, cỡ `slide-16x9` (1280 × 720), nằm ở `assets/diagrams/`. Nhãn bằng tiếng Việt, thuật ngữ Figma giữ tiếng Anh. Đã chạy `self_check.py` (đạt) và xem ảnh render từng sơ đồ. Chưa chạy `verify-geometry.py` (không có trong bản cài của skill), nên các quy tắc connector mới được kiểm bằng mắt.

| File | Loại | Cho nhiệm vụ | Ý chính |
|---|---|---|---|
| `hug-fill-fixed.html` | Nested | 2, Auto layout | Bốn cặp cha và con: Fixed, Hug, Fill, và cha Hug cùng con Fill (chữ bị cắt) |
| `min-max-width.html` | Nested | 2, Auto layout | Cùng một con Fill (min 160, max 400) trong ba khung cha 192, 320, 560: chạm min, Fill, chạm max |
| `variable-alias-chain.html` | Dependency | 1, Variables | Button và Link dùng `color/action/fill`, biến này trỏ về `blue-500` (Light) và `blue-300` (Dark); đường nét đứt màu cam là lỗi trỏ thẳng primitive |
| `component-set-properties.html` | Tree | 3, Component | Component set Button và bốn loại property: Variant, Boolean, Text, Instance swap |
| `file-structure-clean.html` | Tree | Mở đầu, tổ chức file | File gồm Cover, Components, Screens, Handoff, _Archive; Screens chứa section Booking và hai frame đặt tên theo quy ước |
| `breakpoints-modes.html` | Nested | 4, Breakpoints | Cùng ba thẻ: một, hai, ba cột ở Compact, Medium, Expanded; ba frame lấy ba mode của một collection Breakpoint |

Lưu ý khi dùng:
- Hug và Fill xung đột ở `hug-fill-fixed.html` dựa trên quan sát qua API (mục I), chưa thử bằng thao tác tay trong giao diện.
- Khoảng breakpoint (dưới 600, 600 đến 839, 840 đến 1199) lấy từ Material Design 3, đơn vị dp; trong Figma tính theo px. Figma không có breakpoint tự động: mỗi breakpoint là một frame cộng một mode.
- Sơ đồ alias dùng mode ở collection semantic trỏ về primitive một mode, đúng mẫu thông dụng. Câu hỏi "alias giữa collection có chọn được mode không" (trường hợp primitive nhiều mode) vẫn chưa kiểm.
- Cỡ slide chừa 40px lề; nếu template deck có thanh chân thì cần chừa thêm 80px dưới (trong cả sáu sơ đồ, phần nội dung kết thúc trước y = 650).
- Chưa xuất PNG hay SVG cho slide; làm khi cần (`/export-diagram`).

## K. Research thêm cho bản deck khoảng 40 slide (2026-11-24)

Ba subagent haiku đã tra cứu thêm; báo cáo thô nằm ở thư mục tạm của session (r7 chủ đề Figma bổ sung, r8 prototyping và handoff, r9 tư liệu dạy). Mục này chỉ giữ kết luận. Mức chắc theo từng dòng: `official` là trang Figma đọc được, `unverified` là đoạn tìm kiếm hoặc nguồn thứ cấp.

### K1. Chủ đề Figma bổ sung (nguồn Figma Help, trang không ghi ngày)
- **Auto layout:** có Wrap; "absolute position" đã đổi tên thành **Ignore auto layout**; gap có chế độ tự động Between, Around, Evenly (official). Cần sửa lesson và 3 slide đang dùng tên "absolute position".
- **Constraints so với auto layout:** constraint không áp cho con của auto layout trừ khi bật Ignore auto layout (unverified).
- **Layout grid** đã đổi tên thành **layout guide** từ tháng 5/2025 (official); lesson hiện chưa nhắc.
- **Styles so với variables:** variables có alias và mode, styles gom nhiều thuộc tính nhưng không alias được; variables gắn được vào text style và color style (official).
- **Variables:** 6 loại (color, number, string, boolean, timing, easing), tối đa 5.000 variable mỗi collection, publish được; giới hạn publish theo gói chưa tìm được.
- **Component:** Slots có trên mọi gói (Cmd hoặc Ctrl + Shift + S để chuyển đổi), preferred instances (official). Chưa có nguồn cho cách tìm detached instance và phần description.
- **Phím tắt chính thức:** Shift A (thêm auto layout), Option hoặc Ctrl Alt K (tạo component), Cmd hoặc Ctrl D (nhân bản variant). Phím Detach (Cmd Option B): unverified. Đổi tên layer không có phím riêng.
- Khoảng trống: nested auto layout, stacking order, giới hạn publish theo gói.

### K2. Prototyping, handoff, accessibility
- **Prototype cơ bản có ở mọi gói** (trigger như on click, while hovering, after delay; action như navigate, open overlay, swap overlay, back, scroll to, open URL; animation smart animate, dissolve, push, slide, move in; thời lượng 1 ms đến 10 s). Variables trong prototype, expressions và điều kiện cần gói Professional trở lên (official). Chưa có changelog prototype 2025 đến 2026.
- **Dev Mode:** gói Starter không có; Professional, Organization, Enterprise có. Annotation cần Full seat. Code snippet và variable hiện trong Dev Mode. Flexbox 2026: Between với một child căn đầu chứ không căn giữa, gap không âm (official). **Mâu thuẫn chưa phân xử:** trang statuses liệt kê gói Professional đặt được "Ready for dev", trang ready-for-dev view thì không.
- Mục Dev Mode 2026 (agent, Code layers, motion): chỉ thấy trong đoạn tìm kiếm, không dùng.
- **Accessibility, WCAG 2.2** (official): contrast 4,5:1 cho chữ thường và 3:1 cho chữ lớn; mục tiêu chạm tối thiểu 24 × 24 (AA), 44 × 44 (AAA). Con số 48dp của Material và 44pt của Apple: unverified.
- Checklist handoff của Material, Carbon, Primer, Polaris, GOV.UK: chưa nghiên cứu.
- Mô tả việc làm (mục E) cho thấy prototyping 10 trên 12 và handoff 5 trên 12; đây là lý do cân nhắc thêm phụ lục.

### K3. Tư liệu dạy
- **Ví dụ dựng mẫu:** product card, settings row, button set, form field, navbar, pricing card, mỗi cái có cấu trúc layer, auto layout, property và tên variable. Chỉ navbar có nguồn đã mở (Noble Desktop); năm ví dụ còn lại là đề xuất suy luận, cần kiểm trước khi dạy.
- **15 bài tập và bài "sửa file hỏng":** chỉ bài navbar có nguồn đã mở; các bài Gumroad Auto Layout Playground, Frontend Masters, uxplanet chỉ thấy trong tìm kiếm; phần còn lại (tràn text, badge bằng padding, input không full width, tag không wrap, variable alias, mode Dark, button variant, tên layer, breakpoint) là đề xuất.
- **40 câu kiểm tra nhanh** (10 mỗi chủ đề variables, auto layout, components, breakpoints), mỗi câu có đáp án và lỗi hiểu nhầm. Đây là đề xuất của subagent, không lấy từ nguồn. Cần sửa: câu về "absolute position" đổi thành Ignore auto layout; câu "Figma có tự đổi mode theo chiều rộng frame không" chỉ dựa trên feature request, cần kiểm.
- **Quy tắc đặt tên đã mở:** Figma Help (`Button/primary/hover`), blog Figma, Carbon (`text-primary`, `button-primary-active`), Atlassian (`color.background.danger.bold.hovered`). Material 3 và Primer: không mở được trang gốc.
- **Cơ sở học tập cho "làm trước, giải thích sau":** Sinha và Kapur (2021, Review of Educational Research, 91(5), 761-798): 53 nghiên cứu, 166 so sánh, Hedges' g khoảng 0,87 theo tóm tắt thứ cấp, **chưa mở abstract gốc**; Kapur (2016); Kirschner, Sweller và Clark (2006); Atkinson và cộng sự (2000). Hai nguồn sau không ủng hộ dạy không hướng dẫn cho người mới; vì vậy cách dạy "làm ngay, không demo" của buổi này cần được nêu là lựa chọn của người hướng dẫn, kèm sự giám sát và sửa tại chỗ. Chỉ có thông tin thư mục, chưa đọc toàn văn.
- Forum Figma gợi ý hai collection (Page và Brand) cho hệ thống nhiều brand có light và dark. Feature liên kết breakpoint tự động với variable mới là feature request.
