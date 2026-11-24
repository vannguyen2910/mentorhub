---
title: "UI Foundations: Building in Figma"
summary: "Dựng concept đã chọn thành file Figma chạy được ở hai kích thước, bằng variables, auto layout, component và mode."
subtitle: "Dựng concept đã chọn thành file Figma chạy ở hai kích thước"
type: lesson
program: private-training
tags: [figma, design-systems, visual-design, private-training, beginner]
level: beginner
duration: "90 min"
date: 2026-11-24
draft: true
slides: "https://claude.ai/artifact/LGLDrbqwhnSiXAHq955s1F"
source: adapted-from-private-session
previous-session: "UI Fundamentals. Output: chosen-concept.png, decision sheet và token set."
next-session: "Design System. Dùng lại variables và component của buổi này, thêm quy tắc đặt tên theo atomic."
programs: [ui-ux-fundamentals:06b]
---

## Overview

Một file Figma chạy được không bắt đầu từ màn hình đẹp. Nó bắt đầu từ ba thứ mà người khác nhìn vào là hiểu: màu và khoảng cách đến từ đâu, layout co giãn theo luật nào, và phần tử lặp lại được dựng một lần hay chép nhiều lần.

Buổi này là buổi dựng. Học viên đã có concept, decision sheet và token set từ buổi UI Fundamentals, nên không dạy lại vì sao chọn giá trị nào. Buổi chỉ chuyển các giá trị đó thành variables, dựng màn hình bằng auto layout, biến phần tử lặp lại thành component, và cho cùng một component chạy ở hai kích thước màn hình bằng mode.

Mỗi nhiệm vụ mở bằng 4 đến 5 phút sửa lỗi trên một file mẫu "xấu", rồi học viên làm trên concept của học viên. File mẫu chứa sẵn các lỗi người mới hay gặp, nên lỗi được thấy trước khi được giải thích.

**Hình dạng buổi.** Mở đầu 10 phút kiểm file, bốn nhiệm vụ (variables, auto layout, component và variants, breakpoints và modes), phần kết 6 phút gồm 3 phút dự phòng. Học viên làm ngay từ đầu, không có phần demo trước; người hướng dẫn chỉ ra chỗ sai và sửa cùng học viên khi đang làm.

Buổi này thuần kỹ thuật và không dùng AI.

---

## Learning Objectives

Sau buổi này, học viên có thể:

1. **Kiểm tra** file của học viên theo guide: pages, tên layer và cấu trúc đủ rõ để người khác tìm được đường.
2. **Tạo** hai collection variables (primitive và semantic) từ token set của học viên và gắn vào layer, thay cho màu và số gõ tay.
3. **Dựng** layout linh hoạt bằng auto layout, dùng đúng Hug, Fill, Fixed, min và max, với spacing, màu và cỡ chữ lấy từ variables.
4. **Tạo** component và variants từ concept của học viên, dùng đúng loại property (variant, boolean, text, instance swap).
5. **Điều chỉnh** layout và component cho ít nhất hai kích thước màn hình bằng một mode của variables.
6. **Giải thích** quan hệ giữa main component, instance và override, và biết khi nào sửa bản gốc thay vì sửa instance.

---

## Success Check

File có pages, tên layer và cấu trúc rõ. Màu và spacing trong file lấy từ variables, không còn giá trị gõ tay ở phần đã dựng. Một component set chạy được ở ít nhất hai kích thước màn hình.

---

## Materials Needed

- Figma gói Pro của học viên (cần cho nhiều mode ở Nhiệm vụ 4, xem mục Limitations).
- File của học viên, đã dọn theo guide ở mục Pre-Class Preparation.
- Ba thứ từ buổi UI Fundamentals: `chosen-concept.png`, decision sheet, token set.
- File mẫu "xấu" trong Figma, học viên nhân bản về tài khoản của học viên. `[to confirm]` Link và quyền chia sẻ (xem, nhân bản); file hiện nằm ở bản nháp của người hướng dẫn.
- Sáu sơ đồ trong `assets/diagrams/`, ảnh `assets/bad-file-sample-screen.png` và tám ảnh chụp giao diện Figma của người hướng dẫn trong `assets/screens/` (panel Variables, Styles, Text styles, menu thêm style, panel Auto layout, component set Button, Main và Instance, property của TextField).

---

## Pre-Class Preparation

Học viên dọn file theo guide dưới đây trước buổi, khoảng 20 đến 30 phút. Việc dọn file không làm trong buổi; 10 phút đầu buổi chỉ dùng để kiểm kết quả.

### Guide dọn file

1. Tạo file mới, đặt tên theo mẫu `Tên-dự-án_UI-Foundations`.
2. Tạo các page: `Cover`, `Components`, `Screens`, `Handoff`, `_Archive`. Page `Handoff` có thể để trống cho đến khi có bản chốt.
3. Đưa `chosen-concept.png` vào page `Screens`, làm ảnh tham chiếu đặt cạnh nơi sẽ dựng màn hình.
4. Đặt tên layer theo vai trò, không theo hình dạng: `card`, `title`, `cta`, không phải `Frame 12` hay `Rectangle 3`. Frame của màn hình đặt tên theo mẫu `Tên-màn/Mobile`.
5. Chuyển mọi bản nháp, ảnh thử và frame cũ sang page `_Archive`.
6. Có bảng token set (spacing, cỡ chữ, vai trò màu) ở dạng đọc được, để sao chép giá trị khi vào Nhiệm vụ 1.
7. Mở file mẫu "xấu", nhân bản về tài khoản của học viên và kiểm tra mở được.
8. Kiểm tra gói Figma của tài khoản đang dùng: số mode cho phép mỗi collection.

---

## Session Plan

| Thời gian | Block | Nội dung |
|---|---|---|
| 0:00 đến 0:10 | Mở đầu, 10 phút | Kiểm file đã dọn, chốt concept sẽ dựng |
| 0:10 đến 0:25 | Nhiệm vụ 1, Variables, 15 phút | 4 phút sửa file mẫu, 11 phút dựng token set |
| 0:25 đến 0:46 | Nhiệm vụ 2, Auto layout, 21 phút | 5 phút sửa file mẫu, 16 phút dựng màn hình |
| 0:46 đến 1:10 | Nhiệm vụ 3, Component và variants, 24 phút | Biến hai đến ba phần tử lặp lại thành component |
| 1:10 đến 1:24 | Nhiệm vụ 4, Breakpoints và modes, 14 phút | Một mode mới, một breakpoint thứ hai |
| 1:24 đến 1:30 | Kết, 6 phút | Rà success check, ghi việc còn dở thành homework |

Tổng 90 phút. Buffer 3 phút nằm trong phần Kết. `[to confirm]` Deck có 42 slide và phần mở rộng ở mục 6 (cùng phần 6, Handoff) chưa được chia thời lượng: 90 phút đã kín với bốn nhiệm vụ. Cần quyết định rút bớt phần làm hoặc kéo dài buổi. Nếu buổi chạy quá giờ, Nhiệm vụ 3 rút còn hai component; Nhiệm vụ 4 không cắt.

---

## Core Content

### 1. Mở đầu: kiểm file

**Ví dụ trước.** Một designer mở file của đồng nghiệp để dựng tiếp. Trang đầu có ba màn hình tên `Frame 1`, `Frame 1 copy` và `Frame 1 final 2`, kèm một ghi chú "NHÁP, đừng xoá". Không ai biết bản nào là bản cuối, nên việc đầu tiên là hỏi lại người làm. Đó là một file không tự giải thích được.

**Phép thử.** Một người lạ mở file và, trong 30 giây, tìm được ba thứ: màn hình đang làm, nơi chứa component, và bản đã chốt.

Cấu trúc nhắm tới có năm page, mỗi page một việc: `Cover`, `Components`, `Screens`, `Handoff`, `_Archive`. Trong `Screens`, các frame gom theo section và đặt tên theo quy ước `Tên-màn/Thiết-bị`. Sơ đồ: [file-structure-clean.html](../assets/diagrams/file-structure-clean.html).

Lỗi thường gặp (quan sát từ forum Figma và blog, không phải tài liệu chính thức [8]):

- Layer giữ tên mặc định (`Frame 123`, `Rectangle 47`), nên layers panel là một dãy tên vô nghĩa.
- Một page chứa tất cả, lẫn nháp và bản cuối.
- Không có page hoặc dấu hiệu cho bản đã chốt, nên người nhận bàn giao không biết bản nào đúng.

Tổ chức file là khoảng trống của hầu hết giáo trình Figma công khai [8], vì vậy phần này được giữ ở đầu buổi và trong guide gửi trước.

### 2. Variables

**Ví dụ trước.** Trên màn hình của file mẫu có ba nút cam. Nhìn bằng mắt thì cùng một màu, nhưng mã màu là `#E8590C`, `#E8590D` và `#e75a0c`, tức ba giá trị gõ tay. Nếu thương hiệu đổi sang một màu cam khác, ba chỗ phải sửa riêng, và đến chỗ thứ tư đã bị bỏ sót.

**Variables là gì.** Variable là một giá trị có tên (màu, số, chuỗi, boolean) dùng lại ở nhiều nơi. Đổi giá trị ở một chỗ thì mọi layer gắn với nó đổi theo. Variables nằm trong các collection; mỗi collection có một hoặc nhiều mode [1].

**Hai collection, hai lớp.**

- **Primitive** giữ giá trị thô và tên theo giá trị: `blue-500`, `blue-300`, `space-16`.
- **Semantic** giữ tên theo vai trò và trỏ về primitive bằng alias: `color/action/fill` trỏ về `blue-500`.
- Layer và component chỉ dùng semantic. Khi đổi theme hoặc thương hiệu, chỉ semantic được trỏ lại.

Sơ đồ: [variable-alias-chain.html](../assets/diagrams/variable-alias-chain.html). Trong sơ đồ, collection semantic có hai mode (Light, Dark), mỗi mode trỏ về một primitive; đường nét đứt màu cam là lỗi trỏ thẳng từ component vào primitive.

**Đặt tên theo vai trò, không theo màu.** `color/action/fill` vẫn đúng khi màu đổi từ xanh sang cam, còn `blue-main` thì sai ngay lúc đổi. Tên dạng đường dẫn (`color/action/fill`) cũng làm nhóm biến tự gom trong panel.

**Phạm vi buổi này.** Hai collection, ba nhóm (spacing, vai trò màu, cỡ chữ). Giá trị lấy từ token set của buổi UI Fundamentals, nên không dạy lại thang 8pt hay type scale. Modes chưa dạy ở đây, để dành cho Nhiệm vụ 4. Quy tắc đặt tên đầy đủ theo atomic (`a/m/o`) thuộc buổi Design System.

Lỗi thường gặp (forum Figma và blog [8]):

- Đã có variable nhưng vẫn dán mã màu trực tiếp, vì tạo xong bảng màu rồi quên gắn vào layer.
- Dùng primitive thẳng trong component, bỏ qua lớp semantic.
- Đặt tên theo màu (`Blue`, `Main color`).
- Tạo quá nhiều collection khi chưa cần; hai collection (primitive và semantic) đủ để bắt đầu.

Figma có công cụ Check designs để tìm màu gõ tay và gắn lại variable [7].

### 3. Auto layout

**Ví dụ trước.** Ở file mẫu có hàng "Nhắc tôi trước 30 phút", gồm một khung cha và một khung con. Cha để Hug, con để Fill. Kết quả là chữ bị cắt ở "Nhắc tôi trước 3": cha chờ con quyết định chiều rộng, còn con chờ cha. Đây là một cấu hình mâu thuẫn, và triệu chứng là chữ bị cắt chứ không phải một thông báo lỗi.

**Ba cách một khung quyết định kích thước** [3]:

| Chế độ | Ý nghĩa | Khi dùng |
|---|---|---|
| Fixed | Số cố định | Khoảng cách cố định, icon, ảnh có tỉ lệ |
| Hug | Ôm theo nội dung bên trong | Nút, chip, nhãn: cỡ do nội dung quyết định |
| Fill | Lấp đầy phần còn lại của khung cha | Khối nội dung co giãn theo màn hình |

Sơ đồ: [hug-fill-fixed.html](../assets/diagrams/hug-fill-fixed.html).

Ba điều dễ nhầm:

- Fill chỉ có khi khung cha là auto layout và layer con không ở chế độ Ignore auto layout (trước đây gọi là absolute position) [3].
- Gõ một con số vào ô width, hoặc kéo tay một layer cho vừa khít, đều làm layer đó thành Fixed [3].
- Một trục chỉ nên có một bên quyết định kích thước: cha Hug với con Fill là mâu thuẫn. Cách sửa: cha Fixed hoặc Fill, hoặc con Hug.

**Min và max.** Một con Fill thường cần giới hạn: không co hẹp đến mức chữ bị cắt, không giãn quá rộng. Figma cho thêm min width và max width ở ô Width (và tương tự cho height) [3]. Sơ đồ: [min-max-width.html](../assets/diagrams/min-max-width.html), trong đó một con Fill (min 160, max 400) chạm min ở khung cha 192, lấp đầy ở khung cha 320 và chạm max ở khung cha 560.

Trong phiên bản auto layout mới, padding cũng đặt kích thước tối thiểu cho khung: padding 30 mỗi bên thì khung không hẹp hơn 60, và max width không ghi đè điều này [3b].

**Padding và gap lấy từ variables.** Padding và gap (khoảng cách giữa các con) là hai con số đầu tiên nên gắn vào variables spacing đã tạo ở Nhiệm vụ 1. Khi đó đổi thang spacing thì cả màn hình đổi theo.

**Hai phiên bản auto layout.** Từ tháng 7/2026, bản "updated" là mặc định cho frame mới; frame cũ có thể chuyển qua lại đến tháng 1/2027, và component không tự nâng cấp [3b]. `[to confirm]` Hug, Fill, Fixed, min và max có chạy giống nhau ở hai bản trong frame thường hay không (trang help chỉ nói rõ cho Figma Sites). Kiểm trong app trước buổi dạy và ghi lại kết quả.

Lỗi thường gặp (forum Figma và blog [8]):

- Cha Hug, con Fill (đã nêu ở trên).
- Dùng group thay frame để bố cục: group không có auto layout và không co giãn.
- Kích thước Fixed khắp nơi, không có min và max.
- Đặt tay vị trí (x, y) cho các phần tử trong một khung, rồi thêm một dòng chữ dài hơn thì mọi thứ chồng lên nhau.

### 4. Component và variants

**Ví dụ trước.** Ở file mẫu có bốn nút: `Button`, `Button 2`, `Button copy`, `Button final`. Bo góc lần lượt 8, 10, 12 và 9, padding mỗi nút một khác, và còn một component `Button` không ai dùng cùng một bản đã detach. Đổi bo góc của "nút chính" nghĩa là sửa bốn chỗ và đoán xem chỗ nào còn sót.

**Component** là một bản gốc (main component), các bản dùng ở khắp file là instance. Sửa bản gốc thì mọi instance đổi theo; sửa riêng một instance gọi là override. Một component set gom nhiều biến thể của cùng một component, mỗi biến thể là một variant [4].

**Bốn loại property dạy trong buổi** (Figma có năm loại, thêm Slot) [4]:

| Loại | Điều khiển | Ví dụ trên nút |
|---|---|---|
| Variant | Chọn một trong các biến thể | `Size = S, M, L` |
| Boolean | Ẩn hoặc hiện một layer | `Has icon = on, off` |
| Text | Nội dung chữ | `Label` |
| Instance swap | Đổi một component lồng bên trong | `Icon` |

Sơ đồ: [component-set-properties.html](../assets/diagrams/component-set-properties.html).

**Thứ tự nên làm.** Quyết định property trước (Size, Has icon, Label, Icon), rồi mới tạo các variant. Thêm property sau khi đã có nhiều variant thường phải làm lại.

**Phạm vi buổi này.** Hai đến ba phần tử lặp lại của concept (ví dụ nút, thẻ, thanh điều hướng), mỗi phần tử một component. Nhiều hơn một vài component và quy tắc đặt tên theo atomic thuộc buổi Design System.

Lỗi thường gặp (forum Figma và blog [8]):

- Detach instance để sửa nhanh: instance không còn nhận cập nhật từ bản gốc.
- Sửa tay từng instance (override) cho nội dung đổi thường xuyên, thay vì làm thành text property.
- Định nghĩa property sau khi đã tạo variant.
- Đặt tên variant là Yes và No: có nguồn cho biết Figma tự đổi thành boolean và việc gắn variable vào instance không chạy. `[to confirm]` Thử trong app trước khi nêu như một lỗi chắc chắn.
- Component dùng giá trị gõ tay thay vì variables semantic, nên đổi theme không đổi component.

### 5. Breakpoints và modes

**Ví dụ trước.** Một designer có màn hình mobile hoàn chỉnh và được yêu cầu thêm bản desktop. Cách quen tay là nhân bản frame mobile, kéo rộng ra và sửa từng chỗ. Hai tuần sau, màu nút đổi ở mobile mà desktop vẫn cũ, vì hai frame không liên quan gì với nhau ngoài việc từng giống nhau.

**Figma không có breakpoint tự động.** Không có media query trong chế độ thiết kế. Một breakpoint là một frame với kích thước riêng, cộng một mode của variables khi giá trị cần đổi (spacing, cỡ chữ, padding của màn hình). Các component dùng chung và các variables semantic giữ hai frame luôn khớp nhau.

**Ba nhóm kích thước.** Buổi dùng cách chia của Material Design 3 [5]: Compact dưới 600dp, Medium từ 600 đến 839dp, Expanded từ 840 đến 1199dp. Trong Figma, đơn vị tính theo px.

**Cách làm.**

1. Tạo collection `Breakpoint` với ba mode: Compact, Medium, Expanded. Gói Professional cho tối đa 10 mode mỗi collection [2].
2. Tạo vài variable kiểu số cho thứ cần đổi theo kích thước, ví dụ `screen/padding` và `type/body/size`, mỗi mode một giá trị.
3. Gắn variables vào layer, rồi đặt mode cho từng frame: frame Compact dùng mode Compact, frame Expanded dùng mode Expanded.
4. Kiểm tra component co giãn đúng: các thẻ xếp lại thành một, hai hoặc ba cột nhờ auto layout với Fill và min width, chứ không phải nhờ mode.

Sơ đồ: [breakpoints-modes.html](../assets/diagrams/breakpoints-modes.html). `[to confirm]` Việc xếp lại số cột bằng auto layout dạng wrap với Fill và min width có chạy đúng như sơ đồ trong bản auto layout mới hay không; thử trong app.

Lỗi thường gặp (forum Figma và blog [8]):

- Nhân bản frame rồi sửa từng bản, nên hai bản lệch nhau.
- Tìm nút "breakpoint" trong Figma và không thấy.
- Con Fill không có min width: thu hẹp màn hình thì chữ hoặc nút bị bóp quá mức.
- Mode áp theo từng frame, nên một layer lồng bên trong có thể giữ mode khác; kiểm tra mode ở frame ngoài cùng.

`[to confirm]` Alias giữa collection có chọn được mode không khi collection primitive có nhiều mode: nguồn cộng đồng cũ nói không. Buổi này dùng mẫu semantic nhiều mode trỏ về primitive một mode, mẫu này không phụ thuộc câu hỏi trên.

---

### 6. Nội dung mở rộng theo từng phần

Deck gồm 48 slide, tất cả đều là slide chính. Phần này ghi các nội dung được thêm vào ngoài bốn nhiệm vụ gốc, gom theo phần của buổi. Thời lượng cho các nội dung này chưa được chia lại (xem Session Plan).

**Phần 1, File check**
- Đặt tên cho ba loại thứ: layer theo vai trò (`card`, `title`, `cta`), variable theo vai trò có đường dẫn (`color/action/fill`), component nhóm trước trạng thái sau (`Button/Primary/Hover`). Carbon dùng `text-primary`, `button-primary-active`; Atlassian dùng `color.background.danger.bold.hovered`. Material 3 và Primer chưa mở được trang gốc.

**Phần 2, Variables**
- Sáu loại variable: color, number, string, boolean, timing, easing. Tối đa 5.000 variable mỗi collection, publish được; giới hạn publish theo gói chưa xác nhận. Scope giới hạn nơi variable hiện ra.
- Styles so với variables: styles gom nhiều thuộc tính và không alias; variables có alias và mode, và gắn được vào text style và color style.

**Phần 3, Auto layout**
- Wrap cho danh sách có số phần tử thay đổi; gap tự động Between, Around, Evenly.
- Ignore auto layout (trước đây gọi là absolute position) cho phần tử nằm ngoài flow, như badge ở góc.
- Constraints so với auto layout: constraint neo vào cạnh khung cha; auto layout sắp xếp theo luật. `[to confirm]` Constraint của con trong auto layout chỉ có tác dụng khi con bật Ignore auto layout.
- Layout guide (tên mới của layout grid từ 5/2025): grid, columns, rows; baseline bằng row guide kiểu Top. `[to confirm]` Cài đặt baseline.
- Ví dụ dựng mẫu: settings row. Ví dụ là bản nháp do chương trình đề xuất, chưa có nguồn công bố.

**Phần 4, Components**
- Main component là bản gốc; instance nối với bản gốc. Override là thay đổi chỉ ở một instance, phần đã override không đổi theo bản gốc; Reset overrides đưa về bản gốc và giữ liên kết; detach cắt liên kết. Go to main component để mở bản gốc. `[to confirm]` Tên lệnh và vị trí menu trong giao diện hiện tại; override đôi khi mất sau khi publish hoặc đổi variant của component cha (nguồn forum).
- Nested instance (Expose properties from, Nested instances), Slot (loại property thứ năm, có trên mọi gói, Cmd hoặc Ctrl + Shift + S), preferred instances.
- Ví dụ dựng mẫu: button set (Style, Size, State). Bản nháp do chương trình đề xuất.
- Ba phím tắt: Shift A (thêm auto layout), Option K hoặc Ctrl Alt K (tạo component), Cmd D hoặc Ctrl D (nhân bản variant). Phím Detach chưa xác nhận nên không dạy.

**Phần 5, Breakpoints**
- Ví dụ dựng mẫu: pricing card ở hai kích thước. Số cột đổi nhờ auto layout với Fill và min width, không nhờ mode. Bản nháp do chương trình đề xuất.

**Phần 6, Handoff**
- Dev Mode: gói Starter không có; Professional, Organization, Enterprise có; annotation cần Full seat; code snippet và variable hiện trong Dev Mode. Từ tháng 7/2026 code khớp flexbox hơn (Between với một con căn đầu, gap không âm). `[to confirm]` Gói Professional có đặt được Ready for dev hay không (hai trang help mâu thuẫn).
- Checklist trước khi bàn giao: sáu điều tổng hợp từ best practices của Figma và lỗi của file mẫu; không phải checklist chính thức.
- Accessibility theo WCAG 2.2: tương phản 4,5:1 cho chữ thường, 3:1 cho chữ lớn (từ 18pt hoặc 14pt đậm); mục tiêu chạm tối thiểu 24 × 24 (AA), 44 × 44 (AAA).
- Prototype không nằm trong buổi này vì đã có lesson riêng.

**Ảnh chụp giao diện.** Deck có sáu slide ảnh chụp từ một file design system mẫu của người hướng dẫn: panel Variables (collection, group, alias), Styles (text style, menu thêm style gồm Animation và Layout guide), panel Auto layout (Flow, Resizing, Gap, Padding), Main và Instance, ma trận button set, và property của TextField (variant, boolean, instance lồng). Ảnh xác nhận tên panel là Variables và tên Layout guide trong menu Styles; ảnh chưa cho thấy menu Resizing (min và max), Ignore auto layout, Go to main component và Dev Mode.

**Kiểm tra nhanh.** Bốn câu cuối buổi (variables, auto layout, component, breakpoint). Bộ 40 câu đầy đủ, mỗi câu có đáp án và lỗi hiểu nhầm, là đề xuất của chương trình và nằm trong `learning/research.md`.

---

## File mẫu xấu

File mẫu chứa 8 dấu hiệu dưới đây. Mỗi dấu hiệu được bắt ở một block của buổi.

| # | Dấu hiệu | Bắt ở |
|---|---|---|
| 1 | Tên layer mặc định (`Frame 1`, `Rectangle 3`) | Mở đầu |
| 2 | Một page lẫn nháp và bản cuối | Mở đầu |
| 3 | Mã màu gõ tay, ba sắc cam và nhiều xám gần giống nhau | Nhiệm vụ 1 |
| 4 | Group dùng làm bố cục, phần tử đặt tay bằng x, y | Nhiệm vụ 2 |
| 5 | Cha Hug và con Fill (chữ bị cắt) | Nhiệm vụ 2 |
| 6 | Kích thước Fixed khắp nơi, không có min và max | Nhiệm vụ 2 |
| 7 | Nút copy (`Button`, `Button 2`, `Button copy`, `Button final`) thay cho variant | Nhiệm vụ 3 |
| 8 | Instance đã detach và component gốc không ai dùng | Nhiệm vụ 3 |

Ảnh chụp màn hình chính của file mẫu: `assets/bad-file-sample-screen.png`.

---

## Activities

Học viên làm ngay từ đầu trên file của học viên, không có phần demo trước. Người hướng dẫn chỉ ra chỗ sai và sửa cùng học viên khi đang làm.

### Mở đầu: kiểm file (10 phút)

**Setup.** File của học viên đã dọn theo guide; chia sẻ màn hình.

**Task.**
1. Học viên mở file và tự trả lời ba câu của phép thử: đâu là màn hình đang làm, đâu là nơi chứa component, đâu là bản đã chốt.
2. Người hướng dẫn quét layers panel và page list, ghi ra các chỗ chưa rõ.
3. Chốt concept sẽ dựng: mở `chosen-concept.png` cạnh token set.

**Watch-fors.**
- Concept là ảnh thô, chưa có chữ thật: dựng với nội dung giữ chỗ và ghi lại.
- Học viên chưa dọn file: dọn nhanh các lỗi lớn nhất và ghi phần còn lại thành homework, không dành quá 10 phút.

### Nhiệm vụ 1: Variables (15 phút)

**Setup.** File mẫu đang mở ở một tab; token set của học viên ở dạng bảng.

**Task.**
1. (4 phút) Trên file mẫu, tìm ba nút cam gần giống nhau. Tạo một variable và gắn cho một nút để thấy khác biệt giữa giá trị gõ tay và variable.
2. (11 phút) Trên file của học viên, tạo collection primitive (giá trị thô của token set) và collection semantic (tên theo vai trò, alias về primitive) cho ba nhóm: spacing, vai trò màu, cỡ chữ.

**Watch-fors.**
- Đặt tên theo màu thay cho vai trò.
- Gắn component vào primitive, bỏ qua semantic.
- Tạo quá nhiều collection.
- Variable chỉ có tên mà chưa gắn vào layer nào.

### Nhiệm vụ 2: Auto layout (21 phút)

**Setup.** Hai tab: file mẫu và file của học viên; variables đã có từ Nhiệm vụ 1.

**Task.**
1. (5 phút) Trên file mẫu, sửa hàng "Nhắc tôi trước 30 phút" (cha Hug, con Fill) và đổi một group thành frame auto layout.
2. (16 phút) Trên file của học viên, dựng màn hình concept bằng auto layout: Hug cho nút và chip, Fill cho khối nội dung, min và max cho con Fill cần giới hạn. Gắn padding và gap vào variables spacing.

**Watch-fors.**
- Cha Hug với con Fill.
- Gõ số vào width làm layer thành Fixed.
- Phần tử vẫn đặt tay bằng x, y.
- Con Fill không có min width.

### Nhiệm vụ 3: Component và variants (24 phút)

**Setup.** Màn hình đã dựng ở Nhiệm vụ 2 làm nguồn cho component.

**Task.**
1. Chọn hai đến ba phần tử lặp lại (ví dụ nút, thẻ, thanh điều hướng).
2. Quyết định property trước: Size, Has icon, Label, Icon.
3. Tạo component, thêm variants và component property (variant, boolean, text, instance swap); thay các bản cũ bằng instance.
4. Trên file mẫu, thay bốn nút copy bằng instance của một component duy nhất.

**Watch-fors.**
- Detach instance để sửa nhanh.
- Tạo property sau khi đã tạo variant.
- Sửa tay nội dung từng instance thay vì dùng text property.
- Component dùng giá trị gõ tay thay vì variables.

### Nhiệm vụ 4: Breakpoints và modes (14 phút)

**Setup.** Màn hình và component đã dựng ở Nhiệm vụ 2 và 3.

**Task.**
1. Tạo collection `Breakpoint` với ba mode: Compact, Medium, Expanded.
2. Tạo hai đến ba variable số (ví dụ `screen/padding`, `type/body/size`) với giá trị riêng cho từng mode.
3. Nhân bản màn hình thành frame thứ hai, đặt mode khác, điều chỉnh để component co giãn đúng.
4. Kiểm tra component ở cả hai kích thước.

**Watch-fors.**
- Quên đặt mode cho frame, nên giá trị không đổi.
- Con Fill thiếu min width.
- Sửa hai frame riêng thay vì sửa component và variables.
- Gói Figma không đủ mode: dùng hai mode thay cho ba.

### Kết (6 phút)

**Task.**
1. Rà success check cùng học viên: pages và tên layer, variables thay giá trị gõ tay, component set ở hai kích thước.
2. Ghi phần còn dở thành homework.
3. Nhắc buổi sau (Design System) dùng lại variables và component của buổi này.

---

## AI in Practice

Buổi này thuần kỹ thuật và không dùng AI. Lý do: mục tiêu là học viên tự nắm cách Figma xử lý variables, auto layout, component và mode, và phán đoán đúng sai trên file thật. Mục AI in Practice bắt buộc theo quy tắc LP-4 được giữ ở đây dưới dạng ghi chú này, không có prompt thực hành. `[to confirm]` Nếu sau này muốn có phần AI, một hướng hợp lý là dùng sau buổi để rà tên layer và tìm giá trị gõ tay; chưa thử với lớp thật.

---

## Assessment

### Quick knowledge check

1. Ba màu cam gần giống nhau trong một file khác nhau thế nào so với ba layer cùng gắn một variable?
2. Vì sao component nên dùng variable semantic thay vì primitive?
3. Cha Hug và con Fill trên cùng một trục gây ra triệu chứng gì, và có hai cách sửa nào?
4. Khi nào một con Fill cần min width và max width?
5. Figma không có breakpoint tự động. Một breakpoint trong Figma gồm những gì?

### Reflection prompt (homework)

> *"Mở file của bạn và liệt kê ba chỗ còn giá trị gõ tay, tên layer mặc định hoặc kích thước Fixed không cần thiết. Với mỗi chỗ, ghi cách sửa và buổi nào trong khoá sẽ dùng đến nó."*

Homework gồm hai việc: hoàn thiện phần còn dở của bốn nhiệm vụ trong file, và viết phần reflection ở trên.

---

## Limitations

- Phần lớn lỗi thường gặp đến từ forum Figma, blog và bài đăng cộng đồng; số nguồn cho mỗi lỗi chỉ để so sánh tương đối, và một số thread cũ có thể đã lỗi thời [8].
- Phần nhu cầu việc làm dựa trên 12 mô tả công việc đọc trực tiếp (7 Việt Nam, 5 quốc tế), mẫu nhỏ và thiên lệch chọn mẫu, chỉ dùng để chọn trọng tâm. Không nêu tỉ lệ phần trăm nào trong lesson.
- Cặp cha Hug và con Fill bị cắt chữ được quan sát khi dựng file mẫu bằng API, chưa thử bằng thao tác tay trong giao diện.
- Trang help của Figma không ghi ngày cập nhật; nhãn giao diện và giới hạn gói cần kiểm trong app trước khi dạy.
- Thứ tự variables trước auto layout và phương pháp "làm ngay, không demo" là lựa chọn dạy của người hướng dẫn, chưa có nghiên cứu hay lớp thật kiểm chứng.
- Giới hạn của gói Starter với variables và modes chưa xác nhận: bảng so sánh gói để trống ở dòng variable modes, còn trang "Guide to variables" nói variables dùng được trên mọi gói. Buổi này giả định học viên dùng gói Pro.

---

## References

1. Figma Help. "Guide to variables in Figma." https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma (truy cập 2026-11-24). Collection, mode, alias.
2. Figma. "Schema 2025: design systems recap." 2025-10-28. https://www.figma.com/blog/schema-2025-design-systems-recap/. Professional tối đa 10 mode mỗi collection, Organization 20.
3. Figma Help. "Guide to auto layout." https://help.figma.com/hc/articles/360040451373. Hug, Fill, Fixed, min và max; Fill chỉ có với con của auto layout.
   - 3b. Figma Help. Bài về phiên bản auto layout mới. https://help.figma.com/hc/articles/42031586813719. Bản "updated" mặc định từ 2026-07; padding đặt kích thước tối thiểu.
4. Figma Help. "Variants" và component properties. https://help.figma.com/hc/en-us/articles/5579474826519-Variants. Năm loại property; simplified instances bị bỏ từ 2026-03-23.
5. Google. Material Design 3, Window size classes (breakpoints). https://m3.material.io/foundations/layout/applying-layout. Compact dưới 600dp, Medium 600 đến 839dp, Expanded 840 đến 1199dp.
6. Figma Help. Bảng so sánh gói. https://help.figma.com/hc/en-us/articles/360040328273. Dùng để xác định giới hạn gói.
7. Figma Help. "Check designs in Figma." https://help.figma.com/hc/en-us/articles/39592284074263-Check-designs-in-Figma. Tìm màu gõ tay và gắn lại variable.
8. Tổng hợp nội bộ: `learning/research.md` (2026-11-24). Gồm 39 lỗi từ forum Figma và blog, 12 mô tả công việc, 12 giáo trình so sánh; nguồn thứ cấp và ý kiến, không phải tài liệu chính thức.

---

## Further Resources

- Frontend Masters, "Figma for Developers v2" (Steve Kinney): khung gần nhất với thứ tự của buổi (layout, variables, component, responsive bằng modes); 4 giờ 12 phút, có demo và bài tập.
- Tài liệu Design Tokens Community Group, Format Module 2025.10, cho phần mở rộng về token.
- Buổi Design System: quy tắc đặt tên theo atomic và tài liệu hoá hệ thống.

---

*Created by Winnie Nguyen · Private training · Last updated November 2026*
