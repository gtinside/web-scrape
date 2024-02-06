# web-scrape
Utility to scrape NVIDIA events and presentations

## Details
1. NVIDIA Events are being scraped from RSS - https://investor.nvidia.com/rss/event.aspx
2. NVIDIA Presentations are being scraped from RSS - https://investor.nvidia.com/rss/presentation.aspx

## Sample Output
```
[2024-02-06 09:33:19,181] main.py, <module> INFO     --------NVIDIA UPCOMING EVENTS----------------
[2024-02-06 09:33:19,181] main.py, <module> INFO     Event Title: NVIDIA Q4 FY24 Earnings Call
[2024-02-06 09:33:19,181] main.py, <module> INFO     Event Description: https://events.q4inc.com/attendee/382151216
[2024-02-06 09:33:19,181] main.py, <module> INFO     Event Date: 2/21/2024
[2024-02-06 09:33:19,181] main.py, <module> INFO     Event Link: https://investor.nvidia.com/events-and-presentations/events-and-presentations/event-details/2024/NVIDIA-Q4-FY24-Earnings-Call-2024--4s8TN5sqa/default.aspx
[2024-02-06 09:33:19,181] main.py, <module> INFO     ------------------------
[2024-02-06 09:33:19,182] main.py, <module> INFO     Event Title: GTC Financial Analyst Q&A
[2024-02-06 09:33:19,182] main.py, <module> INFO     Event Description: https://video.ibm.com/GTC-Financial-Analyst-QA
[2024-02-06 09:33:19,182] main.py, <module> INFO     Event Date: 3/19/2024
[2024-02-06 09:33:19,182] main.py, <module> INFO     Event Link: https://investor.nvidia.com/events-and-presentations/events-and-presentations/event-details/2024/GTC-Financial-Analyst-QA--2024-AHYjXAy2he/default.aspx
[2024-02-06 09:33:19,182] main.py, <module> INFO     ------------------------
[2024-02-06 09:33:19,266] main.py, <module> INFO     --------NVIDIA UPCOMING PRESENTATIONS----------------
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Title: J.P. Morgan Healthcare Conference
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Description: http://s201.q4cdn.com/141608511/files/doc_presentations/2024/Jan/08/NVIDIA-Accelerating-Healthcare-Innovation-with-AI.pdf
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Date: Mon, 08 Jan 2024 00:00:00 -0500
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Link: https://investor.nvidia.com/events-and-presentations/presentations/presentation-details/2024/JP-Morgan-Healthcare-Conference-2024-gp9J-SvEmB/default.aspx
[2024-02-06 09:33:19,266] main.py, <module> INFO     ------------------------
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Title: December 2023 Shareholder Outreach Meeting Presentation
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Description: http://s201.q4cdn.com/141608511/files/doc_presentations/2023/Dec/07/fall-2023-shareholder-meetings-presentation.pdf
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Date: Thu, 07 Dec 2023 00:00:00 -0500
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Link: https://investor.nvidia.com/events-and-presentations/presentations/presentation-details/2023/December-2023-Shareholder-Outreach-Meeting-Presentation-2023-az12CqTLK7/default.aspx
[2024-02-06 09:33:19,266] main.py, <module> INFO     ------------------------
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Title: NVIDIA Investor Presentation November 2023
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Description: http://s201.q4cdn.com/141608511/files/doc_presentations/2023/11/nvda-f3q24-investor-presentation-final.pdf
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Date: Mon, 27 Nov 2023 00:00:00 -0500
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Link: https://investor.nvidia.com/events-and-presentations/presentations/presentation-details/2023/NVIDIA-Investor-Presentation-November-2023-2023-h6iL8rl2k2/default.aspx
[2024-02-06 09:33:19,266] main.py, <module> INFO     ------------------------
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Title: NVIDIA Investor Presentation October 2023
[2024-02-06 09:33:19,266] main.py, <module> INFO     Presentation Description: http://s201.q4cdn.com/141608511/files/doc_presentations/2023/Oct/01/ndr_presentation_oct_2023_final.pdf
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Date: Sun, 01 Oct 2023 12:00:00 -0400
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Link: https://investor.nvidia.com/events-and-presentations/presentations/presentation-details/2023/NVIDIA-Investor-Presentation-October-2023/default.aspx
[2024-02-06 09:33:19,267] main.py, <module> INFO     ------------------------
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Title: Citi's 2023 Global Technology Conference
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Description: http://s201.q4cdn.com/141608511/files/doc_presentations/2023/Sep/07/citi-global-tech-conference.pdf
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Date: Thu, 07 Sep 2023 00:00:00 -0400
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Link: https://investor.nvidia.com/events-and-presentations/presentations/presentation-details/2023/Citis-2023-Global-Technology-Conference/default.aspx
[2024-02-06 09:33:19,267] main.py, <module> INFO     ------------------------
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Title: NVIDIA Investor Presentation August 2023
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Description: http://s201.q4cdn.com/141608511/files/doc_presentations/2023/08/nvda-f2q24-investor-presentation-final.pdf
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Date: Mon, 28 Aug 2023 00:00:00 -0400
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Link: https://investor.nvidia.com/events-and-presentations/presentations/presentation-details/2023/NVIDIA-Investor-Presentation-August-2023/default.aspx
[2024-02-06 09:33:19,267] main.py, <module> INFO     ------------------------
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Title: Piper Sandler Webinar: Networks for AI
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Description: http://s201.q4cdn.com/141608511/files/doc_presentations/2023/06/27/Networks_for_AI_IR_Webcast_June_2023-FINAL.pdf
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Date: Wed, 28 Jun 2023 00:00:00 -0400
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Link: https://investor.nvidia.com/events-and-presentations/presentations/presentation-details/2023/Piper-Sandler-Webinar-Networks-for-AI/default.aspx
[2024-02-06 09:33:19,267] main.py, <module> INFO     ------------------------
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Title: NVIDIA 2023 Annual Meeting of Stockholders
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Description: http://s201.q4cdn.com/141608511/files/doc_presentations/2023/06/26/Annual_Stockholder_Meeting_23_Final-2.pdf
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Date: Thu, 22 Jun 2023 00:00:00 -0400
[2024-02-06 09:33:19,267] main.py, <module> INFO     Presentation Link: https://investor.nvidia.com/events-and-presentations/presentations/presentation-details/2023/NVIDIA-2023-Annual-Meeting-of-Stockholders/default.aspx
[2024-02-06 09:33:19,268] main.py, <module> INFO     ------------------------
[2024-02-06 09:33:19,268] main.py, <module> INFO     Presentation Title: New Street Research’s Future of Transportation Conference
[2024-02-06 09:33:19,268] main.py, <module> INFO     Presentation Description: http://s201.q4cdn.com/141608511/files/doc_presentations/2023/06/nvda-new-street-auto-6-12-23.pdf
[2024-02-06 09:33:19,268] main.py, <module> INFO     Presentation Date: Mon, 12 Jun 2023 00:00:00 -0400
[2024-02-06 09:33:19,268] main.py, <module> INFO     Presentation Link: https://investor.nvidia.com/events-and-presentations/presentations/presentation-details/2023/New-Street-Researchs-Future-of-Transportation-Conference-2023-4cGia9toz3/default.aspx
[2024-02-06 09:33:19,268] main.py, <module> INFO     ------------------------
[2024-02-06 09:33:19,268] main.py, <module> INFO     Presentation Title: BofA Technology Conference 2023
[2024-02-06 09:33:19,268] main.py, <module> INFO     Presentation Description: http://s201.q4cdn.com/141608511/files/doc_presentations/2023/Jun/06/bofa-tech-conference-6-6-23.pdf
[2024-02-06 09:33:19,268] main.py, <module> INFO     Presentation Date: Tue, 06 Jun 2023 00:00:00 -0400
[2024-02-06 09:33:19,268] main.py, <module> INFO     Presentation Link: https://investor.nvidia.com/events-and-presentations/presentations/presentation-details/2023/BofA-Technology-Conference-2023-2023-YjSWOC19JF/default.aspx

```
