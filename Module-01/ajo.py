def main():
    target = 200000
    weekly = 25000
    weeks = weeks_to_target(target, weekly)
    print(f"Adesola hits his target in {weeks} weeks")

def weeks_to_target(target, weekly):
    saved = 0
    week = 0
    while saved < target:
        week += 1    # increment the week by 1
        saved += weekly
        print(f"Week {week}: ${saved:,.2f}")
    return week

main()
