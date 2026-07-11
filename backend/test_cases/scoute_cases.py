"""
Scoute Test Cases: Sample topic, report, and sources used to evaluate Scoute's synthesizer using DeepEval faithfulness and hallucination metrics.
"""

RESEARCH_TOPIC = "The myth of productivity and the rise of the hustle culture."

RESEARCH_REPORT = """Executive Summary
The glorification of relentless overwork—popularly termed "hustle culture"—has emerged as a defining
feature of the modern professional landscape. Rooted historically in the American Dream and
accelerated by the 2010s technology boom, this ethos positions constant labor and the monetization of
every waking hour as the ultimate measures of human worth. However, contemporary research reveals
that this relentless pursuit of output is built on a fundamental myth: that perpetual activity equates to sustainable productivity.

Key Findings
1. The Historical and Cultural Evolution of "Hustle"
The word "hustle" originates from the 17th-century Dutch term hutselen, meaning "to shake money in a game." Hustle culture is structurally tied to the American Dream ideology. The modern iteration exploded in the 2010s, heavily promoted by the tech community and the rise of the gig economy.

2. The Myth of Productivity and Toxic Productivity
Toxic productivity is an obsessive need to achieve goals at the expense of self-care and relationships. According to Gallup data, 76% of employees experience burnout at least sometimes. Poor mental health severely diminishes motivation, focus, and attention.

3. Systemic Inequalities
For racialized workers, professional environments demand unpaid invisible labor on top of standard duties. Hustle culture disproportionately impacts women who carry the second shift of domestic labor.

4. The Post-Hustle Era: Slow Living
Slow living rejects the idea that productivity is the ultimate human goal. Gen Z increasingly prioritizes mental well-being and career alignment with personal values over relentless wealth accumulation.

Conclusion
The rise of hustle culture successfully rebranded overwork as a moral virtue. However, the data demonstrates that this model is unsustainable. Toxic productivity does not yield better work."""

# Sources retrieved and cited in the report
RESEARCH_SOURCES = [
    {
        "url": "https://www.linkedin.com/pulse/rise-fall-hustle-culture-finding-balance-work-life-karly-gomez-w8t8c",
        "content": "Hustle culture is structurally tied to the American Dream ideology, which asserts that hard work and perseverance inevitably lead to upward mobility."
    },
    {
        "url": "https://www.gallup.com/workplace/288539/employee-burnout-biggest-myth.aspx",
        "content": "76% of employees experience burnout at least sometimes, with 28% reporting feeling burned out very often or always."
    },
    {
        "url": "https://acp-mn.com/about-acp/blog/can-toxic-productivity-affect-our-mental-health",
        "content": "Toxic productivity is an obsessive, uncontrollable need to achieve goals at the expense of self-care, relationships, and overall life balance."
    },
    {
        "url": "https://fortune.com/2024/12/26/what-is-slow-living-trend-tiny-living-unstructured-play-hustle-culture",
        "content": "Burned out workers are ditching hustle culture for the slow living trend, prioritizing well-being over constant productivity."
    }
]