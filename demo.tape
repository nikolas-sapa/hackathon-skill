Output demo.gif
Set Shell bash
Set FontSize 15
Set Width 1100
Set Height 620
Set Theme "Catppuccin Mocha"
Set Padding 24
Set TypingSpeed 15ms

Type "cd ~/Developer/hackathon-skill"
Sleep 300ms
Enter
Sleep 400ms

Type 'python3 scripts/plan.py --hours 48 --team 2 --json-brief'
Enter
Sleep 1800ms

Type 'python3 scripts/scope.py --json '"'"'{"hours_left":10,"features":[{"name":"auth","est_h":3},{"name":"map","est_h":4,"demo_visible":true}]}'"'"' --json-brief'
Enter
Sleep 2200ms

Type 'python3 scripts/idea.py --json '"'"'{"ideas":[{"name":"cli","rubric_fit":4,"demoability":5,"feasibility":4,"sponsor_fit":2},{"name":"platform","rubric_fit":5,"demoability":2,"feasibility":2,"sponsor_fit":4}]}'"'"' --json-brief'
Enter
Sleep 2400ms

Type 'python3 scripts/deadline.py --end 2030-01-01T00:00 --watch'
Enter
Sleep 3400ms
Ctrl+C
Sleep 500ms
