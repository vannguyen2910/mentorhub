---
title: "Hand-Built Prototype"
subtitle: "Nối màn hình thành flow, rồi để người khác bấm thử"
type: lesson
program: standalone
tags: [prototype, figma, interaction, smart-animate, interactive-components, user-testing]
level: junior
duration: "90 min"
date: 2026-11-25
draft: true
previous-session: "Design System. Output: tokens, components and rules for the chosen concept."
next-session: "[to confirm]"
---

## Overview

Một prototype không phải là màn hình đẹp được nối lại với nhau. Nó là một câu hỏi: người dùng có đi được từ đầu đến cuối không, và họ làm gì khi đi lạc. Bạn trả lời câu hỏi đó bằng cách bấm thử.

Buổi này dạy cách dựng prototype bằng tay trong Figma. Bạn tự chọn trigger, action và transition cho từng kết nối. Bạn tự đặt starting point, dựng overlay, đặt tên layer để Smart Animate hoạt động, và tự nối các variant của một component. Không có bước nào do công cụ tự sinh ra. Làm bằng tay buộc bạn hiểu từng kết nối đang làm gì, và khi có lỗi bạn biết tìm ở đâu.

Bạn đã có kiến thức về component và design system từ các bài trước. Buổi này dùng chúng để nối các màn lại với nhau. Đầu ra là một flow bấm được, và bạn có thể đưa nó cho một người khác thử trong vài phút.

Ba điều được đem vào buổi này:

- Vẽ flow trước khi nối. Flow đúng thì nối mới có ích.
- Chọn mức fidelity theo câu hỏi bạn muốn trả lời. Không phải lúc nào cũng cần prototype đầy đủ.
- Tự kiểm tra prototype trước khi đưa cho người khác. Phần lớn lỗi test là lỗi của prototype, không phải của người dùng.

---

## Learning Objectives

Sau buổi này, bạn sẽ có thể:

1. **Vẽ** một user flow cho một task trước khi nối bất kỳ kết nối nào trong Figma.
2. **Chọn** trigger, action và transition phù hợp với từng hành động của người dùng.
3. **Thiết lập** starting point và flow để prototype chạy được từ đầu đến cuối, kèm một overlay.
4. **Đặt tên** layer có chủ đích để Smart Animate chuyển động đúng giữa hai frame.
5. **Dựng** các state của một component bằng variant và interactive component, thay vì nhân bản frame.
6. **Tự kiểm tra** prototype để tìm dead end, state còn thiếu và điều hướng bị lỗi trước khi test.

---

## Success Check

- Bạn có thể chỉ vào một connection và nói trigger, action và transition của nó, cùng lý do chọn từng thứ.
- Khi bấm từ starting point đến màn cuối, bạn không gặp dead end và không cần giải thích thêm.
- Hai frame có chuyển động Smart Animate đều có cùng tên layer ở cùng vị trí trong hierarchy.
- Component có các state được nối bằng variant, không phải bằng frame rời rạc.
- Câu hỏi test của bạn tách được lỗi thiết kế với lỗi prototype: bạn có thể nói lỗi nào là của màn, lỗi nào là do thiếu kết nối.

---

## Materials Needed

- Figma, với quyền tạo file và chế độ Prototype.
- Một task đã chọn từ bài Design System, hoặc task "đặt lịch hẹn" trong Practice Dataset bên dưới.
- Ba đến năm màn của flow, vẽ bằng khung và thanh xám. Chưa cần chữ thật.
- Một bạn học để test nhanh trong buổi (có thể là người ngồi cạnh).

---

## Pre-Class Preparation

- Đọc lại component của bài Design System. Bạn sẽ dùng chúng cho variant.
- Chọn task. Task nên có ít nhất ba bước và một chỗ có thể sai (ví dụ: nhập thông tin sai, chọn giờ đã kín).

---

## Session Plan

| Phút | Phần | Việc làm |
|---|---|---|
| 0–5 | Open | Xem một prototype lỗi và tìm lỗi |
| 5–40 | Theory (3 phần) | Flow trước kết nối, kết nối, Smart Animate và state |
| 40–45 | Bridge | Nghỉ, kiểm tra nhanh, giới thiệu task |
| 45–80 | Practice | Vẽ flow, nối, dựng state, test nhanh |
| 80–88 | Close | Tổng kết, bài tập về nhà, hỏi đáp |
| 88–90 | Dự phòng | Dùng nếu thực hành bị chậm |

---

## Core Content

### Open · Lỗi nằm ở đâu?

Bạn được xem một prototype có ba vấn đề: một màn không có kết nối đi tiếp, một flow không có starting point, và một nút chỉ chạy được khi bấm lần thứ hai.

Thử tự bấm qua prototype này và ghi lại chỗ bạn thấy khựng. Chỗ khựng thường là chỗ có lỗi.

Ví dụ minh họa (bản nháp): người test dừng lại mấy chục giây ở màn không có lối đi tiếp, rồi bỏ cuộc. Nếu chỉ nhìn vào Figma, bạn sẽ không thấy lỗi, vì mọi màn đều có vẻ đúng.

---

### Part 1 · Vẽ flow trước, nối sau

**Hand-built prototype** là prototype bạn dựng bằng tay trong Figma: tự tạo frame, tự nối kết nối, tự chọn cách chuyển màn. Khác với prototype do công cụ sinh ra, mỗi kết nối đều có lý do của bạn đằng sau.

Thứ tự làm việc nên là:

1. Vẽ user flow của task trên giấy hoặc sơ đồ. Liệt kê từng bước người dùng làm.
2. Dựng từng màn tương ứng với bước đó.
3. Nối các màn theo flow.
4. Bấm thử từ đầu đến cuối và sửa chỗ lỗi.
5. Đưa cho một người khác thử.

Ví dụ: một task đặt lịch hẹn có năm bước (chọn dịch vụ, chọn giờ, nhập thông tin, xác nhận, nhận mã). Nếu bạn nối trước khi vẽ flow, rất dễ bỏ sót bước "giờ đã kín" và chỉ phát hiện khi người khác bấm vào.

**Chọn mức fidelity theo câu hỏi.** Low fidelity (khung và thanh xám) đủ để kiểm tra cấu trúc và thứ tự các bước. High fidelity (có animation, state, overlay) nên đến sau, khi cấu trúc đã đứng vững. Dựng high fidelity quá sớm có nghĩa là bạn đánh bóng một giải pháp chưa được kiểm chứng.

Khi nào dùng hand-built prototype? Khi câu hỏi cần trả lời là "người dùng có đi qua được flow không?" hoặc "họ có hiểu bước tiếp theo không?". Khi câu hỏi là "chuyển động có tạo cảm giác tốt không?" thì bạn cần chi tiết hơn.

**Check (30 giây).** Bạn sẽ vẽ flow trước hay nối trước? Vì sao?

---

### Part 2 · Trigger, action, transition và starting point

Mỗi kết nối trong Figma có ba phần:

- **Trigger** là hành động của người dùng: click, hover, drag, bấm phím.
- **Action** là điều xảy ra: đi đến một frame, mở overlay, đóng overlay, quay lại.
- **Transition** là cách màn chuyển: Instant (đổi ngay), Dissolve (mờ dần), Smart Animate (chuyển động theo layer), các kiểu trượt.

Ví dụ: nút "Xác nhận" có trigger là click, action là đi đến màn "Đã đặt lịch", transition là Instant. Nếu đổi transition sang Smart Animate, bạn cần thêm điều kiện ở Part 3.

**Starting point** là điểm bắt đầu của một flow. Mỗi flow cần một starting point trên một frame cấp cao nhất. Một frame có thể thuộc nhiều flow, nhưng chỉ có một starting point. Khi thiếu starting point, một số công cụ test báo lỗi hoặc không chạy được prototype. Đặt tên cho starting point để dễ tìm khi file có nhiều flow.

**Overlay** hiện nội dung trên màn hiện tại mà không rời khỏi màn đó. Dùng overlay cho menu, hộp thoại xác nhận, tooltip và bottom sheet. Dùng action đi đến frame khi người dùng thật sự chuyển sang một màn mới. Trong Figma, Open Overlay giúp giảm thao tác lặp khi bạn nối nhiều overlay giống nhau.

**Hotspot hint** là gợi ý vùng có thể bấm, Figma tự hiện khi bạn di chuột. Người test có thể không thấy gợi ý này, nên đừng để nó quyết định việc họ có tìm được nút hay không.

**Check (30 giây).** Một nút mở một hộp xác nhận, bạn chọn action nào?

---

### Part 3 · Smart Animate và state

**Smart Animate** chuyển động giữa hai frame bằng cách khớp các layer có cùng tên và cùng vị trí trong hierarchy. Nó không đọc nội dung màn hình. Vì vậy:

- Giữ tên layer giống nhau giữa hai frame bạn muốn chuyển động.
- Nhân bản frame thay vì dựng lại từ đầu. Cách này giữ tên nhất quán.
- Giữ mọi layer ở cả hai frame, kể cả layer không hiện ở frame kia. Để ẩn một layer, đặt opacity về 0% thay vì tắt visibility.
- Mở tab Prototype và kiểm tra viền tím: Figma tô các layer nó sẽ khớp. Layer không được tô là layer nó không khớp.

Smart Animate không chuyển động được việc thay đổi nội dung text hay đổi hẳn một vật thể. Khi có nhiều thay đổi cùng lúc, chuyển động có thể bị giật. Đừng dùng Smart Animate cho mọi thứ. Hãy để nó làm chuyển động chính và dùng transition đơn giản cho phần còn lại.

**Variant và interactive component.** Để dựng các state của một component, như Default, Hover, Pressed và Disabled, bạn đặt chúng trong cùng một component set. Sau đó nối các variant bằng kết nối. Với checkbox, bạn chỉ cần hai variant và hai kết nối, thay vì một frame cho mỗi state.

Có ba điều cần nhớ:

- Chỉ nối được các variant trong cùng một component set.
- Tên variant có thể khác nhau (Default, Hover), nhưng layer bên trong các variant phải có tên nhất quán.
- Figma có thể giữ state của component giữa các frame. Nếu state bị kéo sang màn khác, bật Reset component state.

**Check (30 giây).** Hai frame của một nút có tên layer "Label" và "Text" ở hai bên. Smart Animate sẽ làm gì?

---

### Bridge · Nghỉ và giới thiệu task

Nghỉ 2 phút. Sau đó kiểm tra nhanh ba câu: starting point là gì, Smart Animate khớp layer theo tiêu chí nào, và khi nào dùng overlay thay vì một màn mới. Cuối cùng, giới thiệu task thực hành và các bước.

**Cheat sheet:** trigger, action, transition, starting point, overlay, tên layer khớp, variant, Reset component state, viền tím trong tab Prototype.

---

### Practice · Dựng flow và test nhanh (35 phút)

Thực hành trên một task. Mỗi bước có thời gian, và bạn làm liền một mạch. Các bước chi tiết nằm trong file practice.

1. **Vẽ flow (5 phút).** Liệt kê các bước của task và vẽ thành sơ đồ đơn giản.
2. **Nối flow (12 phút).** Dựng ba đến năm màn, nối kết nối với trigger và transition, đặt starting point, thêm một overlay.
3. **Dựng state (8 phút).** Tạo một component có ít nhất hai variant và nối chúng bằng interactive component.
4. **Test nhanh (10 phút).** Bạn đưa prototype cho một bạn học. Họ làm task, bạn chỉ quan sát và ghi lại chỗ họ khựng. Không giải thích.

**Facilitator watch-fors:**
- Học viên nối trước khi vẽ flow, và phát hiện thiếu bước khi đã nối xong.
- Tên layer khác nhau giữa hai frame, rồi họ tưởng Smart Animate lỗi.
- Dùng frame riêng cho từng state thay vì variant.
- Người test hỏi "bước tiếp theo là gì?" và học viên giải thích thay vì quan sát.

---

### Close · Một prototype trả lời một câu hỏi

Prototype tốt trả lời một câu hỏi cụ thể. Trước khi bấm thử, hãy viết câu hỏi đó ra. Câu hỏi quyết định mức fidelity, flow nào cần dựng, và câu hỏi test nào sẽ được đặt.

Bài tập về nhà nằm ở file practice. Bạn nộp một flow hoàn chỉnh kèm câu hỏi test và kết quả một lần test.

---

## Practice Dataset

Nếu bạn không có task của riêng, dùng task sau:

**Đặt lịch hẹn.** Người dùng chọn dịch vụ, chọn ngày và giờ, nhập tên và số điện thoại, xác nhận, rồi nhận mã đặt lịch. Có ba lỗi thường gặp: giờ đã kín, số điện thoại sai định dạng, và người dùng muốn đổi giờ sau khi đã xác nhận.

---

## AI in Practice

### 🤖 Try this with AI

> Đưa cho công cụ AI một task và yêu cầu nó liệt kê các bước của flow kèm các chỗ có thể lỗi:
> *"Liệt kê các bước của task [tên task]. Với mỗi bước, nêu một trường hợp lỗi người dùng có thể gặp."*

### 🧠 Critical thinking prompt

- Các bước AI liệt kê có đủ để dựng flow không?
- Có bước nào AI bỏ qua mà bạn biết người dùng thật sẽ gặp?
- Bạn sẽ đưa những trường hợp lỗi nào vào prototype và bỏ những trường hợp nào?

### ✍️ Prompt engineering tip

Yêu cầu công cụ AI liệt kê các bước theo thứ tự người dùng làm, không theo thứ tự màn hình. Cách này khớp với cách bạn vẽ flow.

### ⚖️ Ethics consideration

Prototype test với người thật cần thông tin rõ ràng về việc họ đang thử gì và dữ liệu nào được ghi lại. Đừng để prototype giả làm một dịch vụ thật khi người test có thể cung cấp thông tin cá nhân.

---

## Assessment

### Quick knowledge check

1. Trigger, action và transition khác nhau thế nào?
2. Khi nào bạn chọn overlay thay vì một màn mới?
3. Vì sao hai frame của Smart Animate cần cùng tên layer ở cùng vị trí trong hierarchy?

### Reflection prompt (homework)

> *"Điểm nào trong flow của bạn khiến người test khựng lại lâu nhất? Là lỗi thiết kế, lỗi prototype, hay bạn chưa biết người dùng cần gì ở bước đó?"*

---

## Further Resources

- [Figma Help: Guide to prototyping in Figma](https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma)
- [Figma Help: Prototype triggers](https://help.figma.com/hc/en-us/articles/360040035834)
- [Figma Help: Present designs and prototypes](https://help.figma.com/hc/en-us/articles/360040318013-Present-designs-and-prototypes)
- [Figma Help: Interactive components fundamentals](https://help.figma.com/hc/en-us/articles/39747190144023-Components-collection-Interactive-components-fundamentals)
- [Figma Best Practices: five ways to improve your prototyping workflow](https://www.figma.com/best-practices/five-ways-to-improve-your-prototyping-workflow/)
- [Maze: how to test Figma prototypes](https://maze.co/blog/test-figma-prototypes/)
- [Lyssna: Figma prototype testing](https://www.lyssna.com/blog/figma-prototype-testing/)

---

*Created by Winnie Nguyen · Standalone · Last updated November 2026*
