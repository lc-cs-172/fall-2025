# Assignment #8: Recursive Merge-Sort

This assignment is designed to show you the benefits of computer science and to
improve your programming skills by using recursion to implement merge_sort, a
best possible algorithm.

## Task

replace the dummy version in `insertion_sort.py` with your own [earlier]
`insertion_sort`; get pytest to pass

replace the dummy version in `merge_sort.py` with your own `merge_sort`
using O(n lg n) time, O(n) space; get pytest to pass

compare basic runtimes for insertion sort and merge_sort (reported by
pytest) and write-up your results

extra credit: explain how you know the timing results are accurate

extra credit: plot the comparision of repeated runtimes, submit the .png files

extra extra credit: implement and analyze `hybrid_sort`
- use insertion_sort at small data sizes within hybrid_sort
- compare the difference in run time with pure merge_sort
- you should run multiple experiments (trials) while varying data sizes
- you should assess the accuracy (depends on trial count and data size)

extra extra extra credit: [this needs Python details I never mentioned] using
only standard Python, implement and verify a checker to ensure that a black-box
in-place sort does a stable sort.  The function signatures are `sort(data)`,
where `data` is a list of objects to sort, and `verify_stable_sort(sort)`, where
`sort` is the sort function to test.

## Logistics

Copy the various program and pytest text files to your local work area.

Modify/replace the program file guts to create working programs.

You will need to have the pytest module installed.  To install pytest,
in a terminal, try

    python3 -m pip install pytest

-or-

    python3 -m pip install --user pytest

[If on debian or MacOS, use --break-system-packages at your own risk.]

Run the modified program under pytest and save the output to a file.
For example,

    pytest merge_sort_test.py > merge_sort_test.txt

You should also be able to invoke pytest like this:

    python3 run_pytest.py merge_sort_test.py > merge_sort_test.txt

You can also run pytest under VS code.

To set up pytest under VS code: visit any .py file and configure `testing`
(click on the flask icon) to use *pytest* (not unittest).  To run pytest, click
on a little invoke icon (a triangle) at the top of the `testing` section in the
left hand pane, or on the banner above the *_test.py file.

Go to this assignment in [LC-CS-172-Fall-2025](https://classroom.google.com);
submit your ASCII text files.

#### [optional enrichment] gritty pytest executable details

This information is for my benefit, you shouldn't need to know this -- the
pytest invocation recipes above should just work.

<!-- I could not make this table work on MacOS, so I used an alternative -- use -- pre-formatted solution -->

		-------------------	|	----------------		
		system				|	pytest location
		-------------------	|	----------------		
		Ubuntu 22.04.5 LTS	|	$HOME/.local/bin/pytest 
		Debian GNU/Linux 12	|	/usr/bin/pytest
		macOS 14.8.1        |   /usr/local/bin/pytest
		RHEL release 8.10	|	/usr/local/bin/pytest
		Ubuntu 22.04.5 LTS	|	/usr/local/bin/pytest
		Windows 11 VS code	|   ...\LocalCache\local-packages\Python313\Scripts[*]

        [*] /mnt/c/Users/Jskud/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0

## Submit

* `assignment_write-up.txt`
* `insertion_sort.py`
* `insertion_sort_test.py`
* `insertion_sort_test.txt`
* `merge_sort.py`
* `merge_sort_test.py`
* `merge_sort_test.txt`
* `run_pytest.py`

Do not forget to hit the submit button.

#### []
