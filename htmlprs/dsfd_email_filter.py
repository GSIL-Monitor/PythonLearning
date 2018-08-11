import re
from collections import defaultdict
from collections import Counter

emailbody = """
	My CoursesCourse Catalog
Recommendations for you.
We combed our catalog and found courses and Specializations that we think match your interests. Browse our recommendations below, and start learning something new today!

Cybersecurity: Developing a Program for Your Business
University System of Georgia | 4 Course Specialization
Starts Oct 31, 2016

Learn to Program: The Fundamentals
University of Toronto
Starts Oct 24, 2016

Executive Data Science
Johns Hopkins University | 5 Course Specialization
Starts Oct 31, 2016

Machine Learning
Stanford University
Starts Oct 31, 2016

Getting and Cleaning Data
Johns Hopkins University
Starts Oct 24, 2016

Practical Machine Learning
Johns Hopkins University
Starts Oct 24, 2016

Journey of the Universe: A Story for Our Times
Yale University | 4 Course Specialization
Starts Oct 24, 2016

Genomic Data Science with Galaxy
Johns Hopkins University
Starts Oct 24, 2016

University of Science and Technology of China | 6 Course Specialization
Starts Oct 25, 2016

Introduction to Genomic Technologies
Johns Hopkins University
Starts Oct 24, 2016

Building a Data Science Team
Johns Hopkins University
Starts Oct 31, 2016

Principles of Computing (Part 1)
Rice University
Starts Nov 14, 2016

Process Mining: Data science in Action
Eindhoven University of Technology
Starts Oct 31, 2016

Mathematical Biostatistics Boot Camp 1
Johns Hopkins University
Starts Oct 24, 2016

Algorithms, Part I
Princeton University
Starts Oct 31, 2016

Foundations of Marketing Analytics
Emory University | 6 Course Specialization
Starts Oct 31, 2016

Investment and Portfolio Management
Rice University | 5 Course Specialization
Starts Oct 24, 2016

Calculus One
The Ohio State University
Starts Oct 31, 2016

Big Data Modeling and Management Systems
University of California, San Diego
Starts Oct 24, 2016

Data Visualization
University of Illinois at Urbana-Champaign
Starts Oct 24, 2016

Financial Engineering and Risk Management Part I
Columbia University
Starts Nov 07, 2016

Programming Mobile Applications for Android Handheld Systems: Part 1
University of Maryland, College Park
Starts Nov 07, 2016

A Crash Course in Data Science
Johns Hopkins University
Starts Oct 31, 2016

Web Application Development: Basic Concepts
University of New Mexico
Starts Oct 24, 2016

Photography Basics and Beyond: From Smartphone to DSLR
Michigan State University | 5 Course Specialization
Starts Oct 31, 2016

Introduction to Big Data
University of California, San Diego
Starts Oct 31, 2016

An Introduction to Interactive Programming in Python (Part 1)
Rice University
Starts Nov 14, 2016

Programming for Everybody (Getting Started with Python)
University of Michigan
Starts Oct 17, 2016

An Introduction to Interactive Programming in Python (Part 2)
Rice University
Starts Nov 14, 2016

Python for Genomic Data Science
Johns Hopkins University
Starts Oct 24, 2016

Data Visualization and Communication with Tableau
Duke University
Starts Oct 31, 2016

Improve Your English Communication Skills
Georgia Institute of Technology | 4 Course Specialization
Starts Oct 24, 2016
"""
emaillist = [emailbody, emailbody, emailbody]


def tokenize(massage):
    massage = massage.lower()
    all_words = re.findall("[a-z0-9']+", massage)
    worddisc = defaultdict(lambda: [0, 0])

    for word in all_words:
        try:
            worddisc[word][0] += 1
            worddisc[word][1] += 1
        except KeyError:
            worddisc[word][0] = 1
            worddisc[word][1] = 1
    # Counter(massage)

    return worddisc

def count_words(training_set):
    counts = {}
    for massage, is_spam in training_set:
        for word in massage:
            try:
                counts[word] += 1
            except KeyError:
                counts[word] += 1
    return counts


aaaa = tokenize(emailbody)
print(aaaa)
