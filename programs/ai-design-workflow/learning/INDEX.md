# Learning: danh mục file

Thư mục này riêng tư; chỉ các file có trong `../SUMMARY.md` lên site. **Mỗi fact có một nhà:** file khác chỉ link, không chép lại.

**Quy tắc đọc:** làm lesson, practice hay outline thì chỉ đọc các file ở ngoài cùng (bảng dưới). `reference/` là kho bằng chứng và khái niệm: chỉ mở khi cần tra một dữ kiện hay một nguồn, không đọc cả thư mục.

## Ngoài cùng: thứ đang chi phối lesson

| File | Nguồn chính của |
|---|---|
| `plan.md` | Cấu trúc chương trình: tuần, lesson hay practice, quyết định, câu hỏi mở |
| `vocabulary.md` | Tên gọi dùng trong chương trình (mỗi ý một tên) |
| `method.md` | Activity flow standard, step card, stage method, 20 gate check |
| `quality-and-measurement.md` | Traceability, alignment check, đo thành công |
| `voice-sample-vi.md` | Mẫu giọng tiếng Việt (quy tắc chính ở `_system/rules/vi-voice.md`) |
| `consistency.json` | Quy tắc cho `_system/scripts/consistency.py` (tên cũ phải biến mất, thứ phải có) |
| `lesson-1-details.md`, `lesson-2-details.md`, `lesson-3-details.md`, `lesson-5-details.md` | Kịch bản activity, nhịp thời gian, chi tiết đã dời khỏi lesson |
| `briefs/` | Content brief của chương trình và của lesson 1, 2, 3, 5 |

## `reference/`: tra cứu, không đọc mặc định

| Nhóm | File |
|---|---|
| AI ở từng stage | `ai-in-discover.md`, `ai-in-insights.md`, `ai-in-prototype.md`, `ai-prototype-foundations.md`, `ai-strengths-and-limits.md` (kèm 100 task) |
| Khái niệm AI | `agentic-ai-concepts.md`, `ai-mental-model-desk-research.md`, `ai-mental-model-harness.md`, `agent-frameworks-product-design.md` |
| Thị trường và nghề | `research.md` |
| Tách từ file khác | `desk-research-competitor-practice.md` (từ `ai-in-discover.md` mục 4) |
| Theo lesson | `source-verification-lesson-1.md`, `five-excerpts-answer-key.md` (đáp án cho người hướng dẫn), `lesson-5-activity-rule-break-hunt.md` |
| Khác | `workflow-design-log.md` (quyết định và sự cố của workspace), `learning-loop-application.md` |

Các file trong `reference/` trùng chủ đề với nhau (ví dụ harness có ở `agentic-ai-concepts.md` mục 5 và `ai-mental-model-harness.md`); gộp lại khi đọc kỹ.

## Đã chuyển ra ngoài `learning/`

| File | Nơi mới |
|---|---|
| `toolkit-refactor-plan.md`, `toolkit-refactor-stage.sh` | `_system/toolkit-refactor/` (script đã sửa đường dẫn) |
| `github-setup-and-publish.md` | `assets/templates/workflow-kit/` (hướng dẫn cho học viên) |
| `lesson-details.md` (cũ, 9 lesson) | `_archive/lesson-details-pre-split-2026-10-30.md` |

`_archive/` giữ file thay thế và file rỗng, có hậu tố ngày. Thêm file mới vào `learning/` thì thêm một dòng vào bảng trên.
