---
title: Hand-Built Prototype (Traditional Figma Prototype), research
status: private working notes
date: 2026-11-25
---

# Hand-Built Prototype: research và learning values

Tài liệu này là nguồn cho bài 90 phút. Không đưa trực tiếp lên site (`learning/` là private).

**Hand-built prototype** ở đây là prototype dựng thủ công trong Figma: tự vẽ frame, tự nối connection, tự chọn trigger, action và transition. Khác với prototype do AI sinh ra hay prototype code. Mục tiêu là hiểu logic flow trước khi bất kỳ công cụ tự động nào làm hộ.

## 1. Kiến thức nền từ nguồn

| Khái niệm | Ý chính | Nguồn |
|---|---|---|
| Trigger, action, transition | Trigger là hành động của người dùng (click, hover, drag). Action là việc xảy ra (navigate, open overlay, scroll). Transition là cách chuyển (Instant, Dissolve, Smart Animate, Move In...) | [Figma Help: Prototype triggers](https://help.figma.com/hc/en-us/articles/360040035834), [Figma Help: Guide to prototyping](https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma), [Arcade: how to prototype in Figma](https://www.arcade.software/guides/how-to-prototype-in-figma) |
| Starting point và flow | Mỗi flow cần một starting point trên top-level frame. Một frame có thể thuộc nhiều flow nhưng chỉ có một starting point. Restart đưa về starting point của flow hiện tại | [Figma Help: Present designs and prototypes](https://help.figma.com/hc/en-us/articles/360040318013-Present-designs-and-prototypes), [dscout: troubleshooting a Figma prototype](https://help.dscout.com/integrations/figma-integration/troubleshooting-a-figma-prototype) |
| Smart Animate | Khớp layer theo tên giữa hai frame. Không animate được đổi nội dung text hay vật thể hoàn toàn khác. Dễ giật khi có nhiều thay đổi cùng lúc. Tên layer là điều kiện quyết định | [Figma Help: Prototyping](https://help.figma.com/hc/en-us/sections/360006534454-Prototyping), [LogRocket: Smart Animate](https://blog.logrocket.com/ux-design/using-figma-smart-animate-prototype-animations/) |
| Overlay | Hiện nội dung trên màn hình hiện tại mà không rời màn chính. Dùng cho menu, modal, tooltip, bottom sheet | [Figma Help: Prototyping](https://help.figma.com/hc/en-us/sections/360006534454-Prototyping) (bài giảng đại học tóm tắt cùng ý) |
| Hotspot hint | Figma tự highlight vùng có thể click. Người test có thể cần gợi ý nếu hint bị ẩn | [Figma Help: Present designs and prototypes](https://help.figma.com/hc/en-us/articles/360040318013-Present-designs-and-prototypes) |
| Interactive component (variants) | Các state (Default, Hover, Pressed, Disabled) nằm trong một component set. Nối variant bằng connection thay vì vẽ từng frame. Ví dụ checkbox: hai variant và hai connection | [Figma Help: Interactive components fundamentals](https://help.figma.com/hc/en-us/articles/39747190144023-Components-collection-Interactive-components-fundamentals), [Smashing: intro to interactive components](https://smashingmagazine.com/2021/07/introduction-figma-interactive-components/) |
| Reset component state | Tắt tính năng giữ state của component giữa các frame, tránh state bị kéo sang màn khác | [Figma Help: Create interactive components](https://help.figma.com/hc/en-us/articles/360061175334) |

## 2. Fidelity: khi nào hand-built là đúng

- Low fidelity test cấu trúc và luồng trước. Prototype tĩnh hoặc chỉ vài kết nối là đủ. Nguồn: [Webflow: low vs high fidelity](https://webflow.com/blog/low-vs-high-fidelity), [Adobe: Prototyping 101](https://blog.adobe.com/en/publish/2017/11/29/prototyping-difference-low-fidelity-high-fidelity-prototypes-use).
- High fidelity (có animation, state, overlay) nên làm sau khi cấu trúc đã đứng vững. Nếu polish trước sẽ tốn công vào đúng giải pháp chưa được kiểm chứng. Nguồn: [Webflow](https://webflow.com/blog/low-vs-high-fidelity), [UXPin: High-fidelity vs low-fidelity](https://www.uxpin.com/studio/blog/high-fidelity-prototyping-low-fidelity-difference/).
- Nielsen Norman Group (qua bản đăng lại trên UXmatters): khi quyết định có làm prototype tương tác hay không, cân nhắc công sức để phản hồi mỗi hành động của người dùng. Nguồn: bản đăng lại trên UXmatters, không có link trực tiếp trong kết quả tìm kiếm. Tìm "Kara Pernice" và "hi-lo fidelity" trên nngroup.com để đọc bản gốc. Chưa xác minh trực tiếp.

## 3. Lỗi thường gặp (dùng làm bài "bắt lỗi")

1. **Không có starting point.** Prototype không chạy đúng hoặc báo lỗi ở một số công cụ test. Nguồn: [dscout](https://help.dscout.com/integrations/figma-integration/troubleshooting-a-figma-prototype).
2. **Dead end.** Màn không có connection nào đi tiếp. Gây misclick và làm người test bối rối. Nguồn: [Maze: test Figma prototypes](https://maze.co/blog/test-figma-prototypes/), [UXtweak: how to test Figma prototypes](https://blog.uxtweak.com/how-to-test-figma-prototypes/).
3. **Chỉ có happy path.** Thiếu validation error, empty state, lỗi mạng, timeout. Nguồn: [Figma prototype testing (Envato Elements)](https://elements.envato.com/learn/figma-prototype-testing).
4. **Hover state trên mobile.** Hover không chạy trên thiết bị cảm ứng. Nguồn: [Qualaroo: 9 common mistakes in prototype testing](https://qualaroo.com/blog/9-common-mistakes-in-prototype-testing-and-how-to-avoid-them).
5. **Không biết lỗi do thiết kế hay do prototype.** Test thất bại nhưng không rõ nguyên nhân, có thể do thiếu connection. Cách hỏi: "Bạn kỳ vọng điều gì xảy ra ở đây?" Nguồn: [Mozilla UX: Let your designs fail for the right reasons](https://blog.mozilla.org/ux/2026/08/let-your-designs-fail-for-the-right-reasons/).
6. **Quyền truy cập và share link.** Người xem cần quyền với cả prototype lẫn file. Một người dùng forum báo flow không hiện trong share link trên trình duyệt. Nguồn: [dscout](https://help.dscout.com/integrations/figma-integration/troubleshooting-a-figma-prototype), [Figma forum: flow starting point](https://forum.figma.com/t/flow-starting-point-doesnt-work/51404).
7. **Prototype quá nặng.** Nhiều ảnh hoặc transition phức tạp gây lag. Gợi ý: giảm kích thước file, thử ở chế độ ẩn danh. Nguồn: [Maze](https://maze.co/blog/test-figma-prototypes/) (ghi chú này lấy từ tóm tắt tìm kiếm, cần đọc lại bài gốc).

## 4. Đặt câu hỏi và kiểm thử

- Mỗi buổi test: một task chính. Nhiều task làm loãng phản hồi. Nguồn: [Lyssna: Figma prototype testing](https://www.lyssna.com/blog/figma-prototype-testing/).
- Số người test thường gợi ý: khoảng 5 người. Nguồn: [Maze](https://maze.co/blog/test-figma-prototypes/) (nguồn thương mại, không phải nghiên cứu độc lập).
- Trước khi tuyển người, tự đi hết mọi đường chính và đường biên. Nguồn: [Maze](https://maze.co/blog/test-figma-prototypes/), [Figma prototype testing (Envato)](https://elements.envato.com/learn/figma-prototype-testing).

## 5. Học liệu gợi ý cho người học

- Figma Help: "Design an interactive button" (khoảng 20 phút, mức trung cấp). Nguồn: [Figma Help](https://help.figma.com/hc/en-us/articles/20953528101783-Design-an-interactive-button).
- freeCodeCamp: interactive button và checkbox (hover, pressed, disabled). Nguồn: [freeCodeCamp](https://www.freecodecamp.org/news/how-to-create-an-interactive-button-component-in-figma/).
- Figma blog: [The Figma prototype challenge: 15 tips in 15 days](https://www.figma.com/blog/the-figma-prototype-challenge/).

## 6. Learning values cho bài 90 phút

Mỗi value là một kết quả học viên làm được sau buổi. Chọn 3 đến 4 cho một buổi.

| # | Learning value | Biểu hiện khi đạt | Gắn với nguồn |
|---|---|---|---|
| LV1 | Đọc và vẽ được flow trước khi nối | Học viên vẽ sơ đồ luồng (user flow) rồi mới nối trong Figma, không nối theo cảm hứng | Mục 2 (fidelity) |
| LV2 | Dùng đúng trigger, action, transition cho từng hành động | Mỗi connection có lý do: click để đi tiếp, overlay cho modal, Instant cho tab | Mục 1 |
| LV3 | Thiết lập starting point và flow đúng | Prototype chạy được từ đầu đến cuối, share được đúng flow | Mục 1 |
| LV4 | Đặt tên layer có chủ đích để Smart Animate chạy | Hai frame khớp tên layer cho chuyển động mượt; học viên biết tên layer quyết định kết quả | Mục 1 |
| LV5 | Dựng state bằng interactive component | Dùng variant cho Default, Hover, Pressed, Disabled thay vì nhân bản frame | Mục 1 |
| LV6 | Tự kiểm tra prototype trước khi test | Học viên đi hết các đường, tìm dead end và thiếu state | Mục 3 |
| LV7 | Thiết kế error và empty state trong flow | Có ít nhất một đường lỗi và một trạng thái trống cho một flow chính | Mục 3 |
| LV8 | Chọn mức fidelity theo mục tiêu test | Giải thích được vì sao chọn low hay high cho một câu hỏi cụ thể | Mục 2 |
| LV9 | Viết câu hỏi test để tách lỗi thiết kế với lỗi prototype | Có câu hỏi mở "bạn kỳ vọng gì ở đây?" trong script test | Mục 3, 4 |

## 7. Gợi ý cấu trúc 90 phút (dự thảo, chưa khóa)

| Phút | Hoạt động | Gắn LV |
|---|---|---|
| 0-10 | Mở đầu: cho xem một prototype lỗi (dead end, không starting point) và hỏi lỗi ở đâu | LV6 |
| 10-25 | Concept: trigger, action, transition, starting point, overlay | LV2, LV3 |
| 25-35 | Demo: nối một flow 3 màn bằng tay, không dùng Smart Animate | LV1, LV2, LV3 |
| 35-55 | Thực hành: dựng flow của một task (đăng nhập hoặc đặt lịch), thêm overlay và một error state | LV2, LV7 |
| 55-70 | Smart Animate và interactive component: đặt tên layer, nối variant | LV4, LV5 |
| 70-82 | Tự kiểm tra và test nhanh với bạn (một người làm, một người click, không giải thích) | LV6, LV9 |
| 82-90 | Phản hồi và chốt: dùng thời điểm nào, mức fidelity nào | LV8 |

Lưu ý: thời lượng là dự thảo. Chỉnh sau khi chốt số learning value và ví dụ.

## 7b. Tips và trick khi dựng prototype

Nguồn chủ yếu là blog và bài community. Mục có dấu (*) cần đọc lại nguồn gốc trước khi dạy.

**Smart Animate và tên layer**
- Duplicate frame thay vì dựng lại từ đầu. Cách này giữ tên layer nhất quán giữa các frame. Nguồn: [Figma Best Practices: five ways to improve your prototyping workflow](https://www.figma.com/best-practices/five-ways-to-improve-your-prototyping-workflow/).
- Giữ mọi layer ở cả hai state. Để ẩn, đặt opacity 0% thay vì tắt visibility. Nguồn: [UX Planet: Smart Animate](https://uxplanet.org/get-the-most-out-of-smart-animate-6403e252227c).
- Smart Animate khớp theo tên và vị trí trong hierarchy. Dropbox Design thêm opacity vào danh sách cần nhất quán. Nguồn: [Figma Help: Smart Animate](https://figma-signup.helpjuice.com/en_US/advanced-prototyping/smart-animate-layers-between-frames), [Dropbox Design](https://dropbox.design/article/illustrating-concepts-using-figmas-smart-animate).
- Mở tab Prototype để xem layer nào được khớp (viền tím). Nguồn: [UX Design: interactive components](https://uxdesign.cc/how-to-use-interactive-components-to-create-functional-buttons-in-figma-in-3-steps-d6efbe065b2c).
- Đổi thứ tự layer giữa các instance có thể gây hiệu ứng lạ. Nguồn: cùng nguồn trên.
- Animation nhanh thì dùng easing tùy chỉnh thay vì mặc định. Nguồn: [Figma Best Practices](https://www.figma.com/best-practices/five-ways-to-improve-your-prototyping-workflow/).
- (*) Hạn chế: Smart Animate không áp cho action overlay (tóm tắt từ tìm kiếm, cần kiểm tra trên trang help hiện hành). Texture và noise sinh ngẫu nhiên, nên nhân bản frame trước khi test. Nested variant override có thể lỗi. Nguồn: [Figma forum: Smart Animate](https://forum.figma.com/archive-21/what-are-the-layer-matching-rules-of-smart-animate-34844).

**Cấu trúc flow và điều hướng**
- Tránh "spaghetti navigation". Nguồn: [Chime: three tips for complex prototypes](https://medium.com/life-at-chime/three-tips-for-building-complex-prototypes-in-figma-bff1878aabb).
- Dùng Open Overlay để giảm thao tác lặp cho modal và menu. Nguồn: [UX Collective: advanced prototyping tips](https://uxdesign.cc/advanced-figma-prototyping-tips-tricks-ccef9db99f24).
- Đặt tên starting point để dễ tìm khi prototype có nhiều flow. Nguồn: [UX Planet: prototyping for beginners](https://uxplanet.org/figma-prototyping-for-beginners-the-basics-features-and-tips-you-should-know-921ce6c0f846).
- Gắn interaction vào component thay vì frame thường để dễ mở rộng. Nguồn: [SSW: interactive prototypes in Figma](https://www.ssw.com.au/rules-beta/figma-prototypes).

**Biến và logic có điều kiện**
- Action Set variable và Conditional (if/else) cho phép prototype có logic. Figma có ví dụ quiz và shopping cart. Nguồn: [Figma Help: conditional prototype](https://help.figma.com/hc/en-us/articles/15339657135383), [Figma blog: 23 prototyping resources](https://www.figma.com/blog/23-prototyping-resources-to-bookmark-right-now/).
- Expression dùng biến để áp logic lên dữ liệu. Nguồn: [UX Collective: variables in Figma](https://uxdesign.cc/the-big-problem-with-variables-in-figma-61a4ea82640).
- (*) Forum có báo cáo lỗi if/else và biến không cập nhật text. Các thread này cũ, cần kiểm tra lại. Nguồn: [Figma forum: conditional logic limitations](https://forum.figma.com/t/issues-with-figma-prototypes-variable-linked-text-not-updating-and-conditional-logic-limitations/84061).

**Tổ chức file**
- Tách file prototype test khỏi file làm việc. Một prototype connection bất kỳ trong file có thể làm hỏng điều hướng < > giữa các frame. Nguồn: [Viget: Figma tips for non-designers](https://www.viget.com/articles/figma-tips-for-non-designers-part-1-structure-ui-basics).
- Có page Prototype riêng, dùng cho user testing và flow chính. Nguồn: [Infinum handbook: design files and project folders](https://infinum.com/handbook/design/design-process/handoff/design-files-and-project-folders).
- Đặt tên nhất quán cho file, page, frame, layer. Frame cấp cao ghi tên sản phẩm và kích thước màn hình, frame lồng ghép đặt tên theo chức năng. Nguồn: [Figma Best Practices: team file organization](https://www.figma.com/best-practices/team-file-organization/).
- Chia sẻ prototype không cấp quyền xem file gốc. Cần cấp quyền riêng nếu người xem cần thấy file. Nguồn: [Viget](https://www.viget.com/articles/figma-tips-for-non-designers-part-1-structure-ui-basics).

**Gợi ý cho LV**
- LV3 (starting point, flow): tách file test và thêm tên cho starting point.
- LV4 (Smart Animate): dạy kỹ viền tím, duplicate frame, opacity 0%.
- LV5 (interactive component): gắn interaction vào component.
- LV6 (kiểm tra): điều hướng < > và kiểm tra share quyền.

## 8. Quyết định về chuỗi bài (Winnie xác nhận 2026-11-25)

- Chuỗi: UI Foundations (Figma) → UI Fundamentals → Design System → Hand-Built Prototype (bài này).
- Học viên đã biết Figma cơ bản từ bài UI Foundations. Không cần dạy lại thao tác cơ bản, chỉ nhắc nhanh (10 phút tối đa).
- Đề xuất bài tập: dựng một flow 3 đến 5 màn cho một task (đăng nhập hoặc đặt lịch) gồm starting point, một overlay, một interactive component có ít nhất hai variant, và một error hoặc empty state. Kèm checklist tự kiểm tra (không dead end, có starting point, đặt tên layer nhất quán) và một buổi test nhanh với bạn học. Nộp link Figma kèm câu hỏi test đã viết.
- Tiêu chí chấm (dự thảo): đủ starting point và flow chạy hết; đúng trigger và transition theo mục đích; tên layer khớp cho Smart Animate; có ít nhất một đường lỗi; câu hỏi test tách được lỗi thiết kế và lỗi prototype.
- Lưu ý: `design-system` và `ui-foundations-figma` xuất hiện ở cả `library/lessons/00-foundation/` lẫn `library/lessons/03-develop/`. Cần xác nhận bản nào là chính trước khi tham chiếu chéo.
