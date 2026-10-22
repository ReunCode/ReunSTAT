import math

def calculate_final_requirements():
    print("โปรแกรมคำนวณคะแนนสอบ 'Final' ที่ต้องทำได้ตามเป้าหมายเกรด")

    midterm_raw = float(input(f"กรอกคะแนนดิบ Midterm ที่ได้ : "))

    if midterm_raw < 0 or midterm_raw > 90:
      print(f"ได้โปรดกรอกคะแนนระหว่าง 0 ถึง 90")
      return

    midterm_weighted = (midterm_raw / 90) * 50

    grading_criteria = {
        "A": 80.0,
        "B+": 75.0,
        "B": 70.0,
        "C+": 60.0,
        "C": 50.0,
        "D+": 40.0,
        "D": 30.0,
        "F": 0.0,
    }

    guaranteed_grade = None
    for grade, min_score in grading_criteria.items():
      if midterm_weighted >= min_score:
        guaranteed_grade = grade
        break

    print(
        f"คะแนน Midterm ที่ได้: {midterm_raw:.2f} / {90.00} คะแนนดิบ"
        f" (คิดเป็น {midterm_weighted:.2f} / {50} คะแนนจริง)"
    )

    if guaranteed_grade:
      print(f"คะแนน Midterm ของท่านได้เกรด {guaranteed_grade} แน่ๆ")

    print(f"{'เกรด':<5} | {'คะแนนไฟนอลที่ต้องได้':<} | {'คะแนนสอบดิบไฟนอล' :<30}")

    for grade, min_total_score in grading_criteria.items():
      needed_weighted = min_total_score - midterm_weighted

      if needed_weighted <= 0:
          print(f"{grade:<5} | การันตีได้เกรดนี้แล้ว if ได้ไข่ต้มในไฟนอล")
          continue

      needed_raw = (needed_weighted / 50) * 90

      if needed_weighted > 50:
        print(
            f"{grade:<5} | ไม่ถึงเกรดแล้ว"
            f" (ต้องใช้ไฟนอล {needed_weighted:.2f} คะแนน)"
        )
      else:
        info_str = (
            f"{grade:<5} | ต้องได้ {needed_weighted:5.2f}/{50} คะแนนจริง "
            f" | ต้องทำได้ {needed_raw:5.2f} /{90} คะแนนดิบ"
        )

        print(info_str)

if __name__ == "__main__":
  calculate_final_requirements()  