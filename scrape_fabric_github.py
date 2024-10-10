import requests
import json

# We would like to acknowledge and thank that the Fabric team that opened up this data set.
# Freely distributed in https://github.com/danielmiessler/fabric/
# Please check their project out and support the initiative - https://github.com/danielmiessler/fabric/blob/main/README.md


# This scraper was built with help of PromptBros.ai
# you can find and use it freely at https://promptbros.ai/agent/cltg5mos80007tpmyzbinuniu?chat=oDr3Iywk6csujhyga9j0cbuuz


# Function to scrape content from a raw GitHub URL
def scrape_system_md(url, pattern_name):
    response = requests.get(url)
    content = response.text

    # Dictionary to store the scraped sections
    sections = {}

    # Splitting the content into lines
    lines = content.splitlines()

    current_section = None

    # Loop through each line to find relevant sections
    for line in lines:
        # Identify the section headings based on '#' prefix
        if line.startswith("# "):
            current_section = line.strip().replace("# ", "")
            sections[current_section] = ''
        elif current_section:
            # Accumulate content for the current section
            sections[current_section] += line + '\n'

    return {
        'title': pattern_name,
        'source': url,
        'content': sections
    }

# List of patterns to scrape, each with its respective URL
patterns_to_scrape = [
    {
        'pattern_name': 'agility_story',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/agility_story/system.md'
    }
,{
        'pattern_name': 'ai',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/ai/system.md'
    }
,{
        'pattern_name': 'analyze_answers',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_answers/system.md'
    }
,{
        'pattern_name': 'analyze_cfp_submission',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_cfp_submission/system.md'
    }
,{
        'pattern_name': 'analyze_claims',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_claims/system.md'
    }
,{
        'pattern_name': 'analyze_comments',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_comments/system.md'
    }
,{
        'pattern_name': 'analyze_debate',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_debate/system.md'
    }
,{
        'pattern_name': 'analyze_email_headers',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_email_headers/system.md'
    }
,{
        'pattern_name': 'analyze_incident',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_incident/system.md'
    }
,{
        'pattern_name': 'analyze_interviewer_techniques',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_interviewer_techniques/system.md'
    }
,{
        'pattern_name': 'analyze_logs',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_logs/system.md'
    }
,{
        'pattern_name': 'analyze_malware',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_malware/system.md'
    }
,{
        'pattern_name': 'analyze_military_strategy',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_military_strategy/system.md'
    }
,{
        'pattern_name': 'analyze_paper',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_paper/system.md'
    }
,{
        'pattern_name': 'analyze_patent',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_patent/system.md'
    }
,{
        'pattern_name': 'analyze_personality',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_personality/system.md'
    }
,{
        'pattern_name': 'analyze_presentation',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_presentation/system.md'
    }
,{
        'pattern_name': 'analyze_product_feedback',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_product_feedback/system.md'
    }
,{
        'pattern_name': 'analyze_prose',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_prose/system.md'
    }
,{
        'pattern_name': 'analyze_prose_json',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_prose_json/system.md'
    }
,{
        'pattern_name': 'analyze_prose_pinker',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_prose_pinker/system.md'
    }
,{
        'pattern_name': 'analyze_sales_call',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_sales_call/system.md'
    }
,{
        'pattern_name': 'analyze_spiritual_text',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_spiritual_text/system.md'
    }
,{
        'pattern_name': 'analyze_tech_impact',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_tech_impact/system.md'
    }
,{
        'pattern_name': 'analyze_threat_report',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_threat_report/system.md'
    }
,{
        'pattern_name': 'analyze_threat_report_trends',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_threat_report_trends/system.md'
    }
,{
        'pattern_name': 'answer_interview_question',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/answer_interview_question/system.md'
    }
,{
        'pattern_name': 'ask_secure_by_design_questions',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/ask_secure_by_design_questions/system.md'
    }
,{
        'pattern_name': 'capture_thinkers_work',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/capture_thinkers_work/system.md'
    }
,{
        'pattern_name': 'check_agreement',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/check_agreement/system.md'
    }
,{
        'pattern_name': 'clean_text',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/clean_text/system.md'
    }
,{
        'pattern_name': 'coding_master',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/coding_master/system.md'
    }
,{
        'pattern_name': 'compare_and_contrast',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/compare_and_contrast/system.md'
    }
,{
        'pattern_name': 'create_5_sentence_summary',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_5_sentence_summary/system.md'
    }
,{
        'pattern_name': 'create_academic_paper',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_academic_paper/system.md'
    }
,{
        'pattern_name': 'create_ai_jobs_analysis',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_ai_jobs_analysis/system.md'
    }
,{
        'pattern_name': 'create_aphorisms',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_aphorisms/system.md'
    }
,{
        'pattern_name': 'create_art_prompt',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_art_prompt/system.md'
    }
,{
        'pattern_name': 'create_better_frame',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_better_frame/system.md'
    }
,{
        'pattern_name': 'create_coding_project',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_coding_project/system.md'
    }
,{
        'pattern_name': 'create_command',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_command/system.md'
    }
,{
        'pattern_name': 'create_cyber_summary',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_cyber_summary/system.md'
    }
,{
        'pattern_name': 'create_formal_email',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_formal_email/system.md'
    }
,{
        'pattern_name': 'create_git_diff_commit',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_git_diff_commit/system.md'
    }
,{
        'pattern_name': 'create_graph_from_input',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_graph_from_input/system.md'
    }
,{
        'pattern_name': 'create_hormozi_offer',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_hormozi_offer/system.md'
    }
,{
        'pattern_name': 'create_idea_compass',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_idea_compass/system.md'
    }
,{
        'pattern_name': 'create_investigation_visualization',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_investigation_visualization/system.md'
    }
,{
        'pattern_name': 'create_keynote',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_keynote/system.md'
    }
,{
        'pattern_name': 'create_logo',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_logo/system.md'
    }
,{
        'pattern_name': 'create_markmap_visualization',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_markmap_visualization/system.md'
    }
,{
        'pattern_name': 'create_mermaid_visualization',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_mermaid_visualization/system.md'
    }
,{
        'pattern_name': 'create_mermaid_visualization_for_github',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_mermaid_visualization_for_github/system.md'
    }
,{
        'pattern_name': 'create_micro_summary',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_micro_summary/system.md'
    }
,{
        'pattern_name': 'create_network_threat_landscape',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_network_threat_landscape/system.md'
    }
,{
        'pattern_name': 'create_npc',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_npc/system.md'
    }
,{
        'pattern_name': 'create_pattern',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_pattern/system.md'
    }
,{
        'pattern_name': 'create_quiz',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_quiz/system.md'
    }
,{
        'pattern_name': 'create_reading_plan',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_reading_plan/system.md'
    }
,{
        'pattern_name': 'create_recursive_outline',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_recursive_outline/system.md'
    }
,{
        'pattern_name': 'create_report_finding',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_report_finding/system.md'
    }
,{
        'pattern_name': 'create_rpg_summary',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_rpg_summary/system.md'
    }
,{
        'pattern_name': 'create_security_update',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_security_update/system.md'
    }
,{
        'pattern_name': 'create_show_intro',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_show_intro/system.md'
    }
,{
        'pattern_name': 'create_sigma_rules',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_sigma_rules/system.md'
    }
,{
        'pattern_name': 'create_story_explanation',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_story_explanation/system.md'
    }
,{
        'pattern_name': 'create_stride_threat_model',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_stride_threat_model/system.md'
    }
,{
        'pattern_name': 'create_summary',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_summary/system.md'
    }
,{
        'pattern_name': 'create_tags',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_tags/system.md'
    }
,{
        'pattern_name': 'create_threat_scenarios',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_threat_scenarios/system.md'
    }
,{
        'pattern_name': 'create_ttrc_graph',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_ttrc_graph/system.md'
    }
,{
        'pattern_name': 'create_ttrc_narrative',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_ttrc_narrative/system.md'
    }
,{
        'pattern_name': 'create_upgrade_pack',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_upgrade_pack/system.md'
    }
,{
        'pattern_name': 'create_video_chapters',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_video_chapters/system.md'
    }
,{
        'pattern_name': 'create_visualization',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_visualization/system.md'
    }
,{
        'pattern_name': 'explain_code',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/explain_code/system.md'
    }
,{
        'pattern_name': 'explain_docs',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/explain_docs/system.md'
    }
,{
        'pattern_name': 'explain_math',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/explain_math/system.md'
    }
,{
        'pattern_name': 'explain_project',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/explain_project/system.md'
    }
,{
        'pattern_name': 'explain_terms',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/explain_terms/system.md'
    }
,{
        'pattern_name': 'export_data_as_csv',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/export_data_as_csv/system.md'
    }
,{
        'pattern_name': 'extract_algorithm_update_recommendations',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_algorithm_update_recommendations/system.md'
    }
,{
        'pattern_name': 'extract_article_wisdom',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_article_wisdom/system.md'
    }
,{
        'pattern_name': 'extract_book_ideas',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_book_ideas/system.md'
    }
,{
        'pattern_name': 'extract_book_recommendations',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_book_recommendations/system.md'
    }
,{
        'pattern_name': 'extract_business_ideas',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_business_ideas/system.md'
    }
,{
        'pattern_name': 'extract_controversial_ideas',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_controversial_ideas/system.md'
    }
,{
        'pattern_name': 'extract_core_message',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_core_message/system.md'
    }
,{
        'pattern_name': 'extract_ctf_writeup',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_ctf_writeup/system.md'
    }
,{
        'pattern_name': 'extract_extraordinary_claims',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_extraordinary_claims/system.md'
    }
,{
        'pattern_name': 'extract_ideas',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_ideas/system.md'
    }
,{
        'pattern_name': 'extract_insights',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_insights/system.md'
    }
,{
        'pattern_name': 'extract_insights_dm',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_insights_dm/system.md'
    }
,{
        'pattern_name': 'extract_instructions',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_instructions/system.md'
    }
,{
        'pattern_name': 'extract_jokes',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_jokes/system.md'
    }
,{
        'pattern_name': 'extract_main_idea',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_main_idea/system.md'
    }
,{
        'pattern_name': 'extract_most_redeeming_thing',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_most_redeeming_thing/system.md'
    }
,{
        'pattern_name': 'extract_patterns',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_patterns/system.md'
    }
,{
        'pattern_name': 'extract_poc',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_poc/system.md'
    }
,{
        'pattern_name': 'extract_predictions',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_predictions/system.md'
    }
,{
        'pattern_name': 'extract_primary_problem',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_primary_problem/system.md'
    }
,{
        'pattern_name': 'extract_primary_solution',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_primary_solution/system.md'
    }
,{
        'pattern_name': 'extract_product_features',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_product_features/system.md'
    }
,{
        'pattern_name': 'extract_questions',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_questions/system.md'
    }
,{
        'pattern_name': 'extract_recommendations',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_recommendations/system.md'
    }
,{
        'pattern_name': 'extract_references',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_references/system.md'
    }
,{
        'pattern_name': 'extract_skills',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_skills/system.md'
    }
,{
        'pattern_name': 'extract_song_meaning',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_song_meaning/system.md'
    }
,{
        'pattern_name': 'extract_sponsors',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_sponsors/system.md'
    }
,{
        'pattern_name': 'extract_videoid',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_videoid/system.md'
    }
,{
        'pattern_name': 'extract_wisdom',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_wisdom/system.md'
    }
,{
        'pattern_name': 'extract_wisdom_agents',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_wisdom_agents/system.md'
    }
,{
        'pattern_name': 'extract_wisdom_dm',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_wisdom_dm/system.md'
    }
,{
        'pattern_name': 'extract_wisdom_nometa',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/extract_wisdom_nometa/system.md'
    }
,{
        'pattern_name': 'find_hidden_message',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/find_hidden_message/system.md'
    }
,{
        'pattern_name': 'find_logical_fallacies',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/find_logical_fallacies/system.md'
    }
,{
        'pattern_name': 'get_wow_per_minute',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/get_wow_per_minute/system.md'
    }
,{
        'pattern_name': 'get_youtube_rss',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/get_youtube_rss/system.md'
    }
,{
        'pattern_name': 'improve_academic_writing',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/improve_academic_writing/system.md'
    }
,{
        'pattern_name': 'improve_prompt',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/improve_prompt/system.md'
    }
,{
        'pattern_name': 'improve_report_finding',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/improve_report_finding/system.md'
    }
,{
        'pattern_name': 'improve_writing',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/improve_writing/system.md'
    }
,{
        'pattern_name': 'label_and_rate',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/label_and_rate/system.md'
    }
,{
        'pattern_name': 'official_pattern_template',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/official_pattern_template/system.md'
    }
,{
        'pattern_name': 'provide_guidance',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/provide_guidance/system.md'
    }
,{
        'pattern_name': 'rate_ai_response',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/rate_ai_response/system.md'
    }
,{
        'pattern_name': 'rate_ai_result',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/rate_ai_result/system.md'
    }
,{
        'pattern_name': 'rate_content',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/rate_content/system.md'
    }
,{
        'pattern_name': 'rate_value',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/rate_value/system.md'
    }
,{
        'pattern_name': 'raw_query',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/raw_query/system.md'
    }
,{
        'pattern_name': 'raycast',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/raycast/system.md'
    }
,{
        'pattern_name': 'recommend_artists',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/recommend_artists/system.md'
    }
,{
        'pattern_name': 'recommend_pipeline_upgrades',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/recommend_pipeline_upgrades/system.md'
    }
,{
        'pattern_name': 'recommend_talkpanel_topics',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/recommend_talkpanel_topics/system.md'
    }
,{
        'pattern_name': 'show_fabric_options_markmap',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/show_fabric_options_markmap/system.md'
    }
,{
        'pattern_name': 'solve_with_cot',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/solve_with_cot/system.md'
    }
,{
        'pattern_name': 'suggest_pattern',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/suggest_pattern/system.md'
    }
,{
        'pattern_name': 'summarize',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/summarize/system.md'
    }
,{
        'pattern_name': 'summarize_debate',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/summarize_debate/system.md'
    }
,{
        'pattern_name': 'summarize_git_changes',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/summarize_git_changes/system.md'
    }
,{
        'pattern_name': 'summarize_git_diff',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/summarize_git_diff/system.md'
    }
,{
        'pattern_name': 'summarize_lecture',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/summarize_lecture/system.md'
    }
,{
        'pattern_name': 'summarize_legislation',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/summarize_legislation/system.md'
    }
,{
        'pattern_name': 'summarize_micro',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/summarize_micro/system.md'
    }
,{
        'pattern_name': 'summarize_newsletter',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/summarize_newsletter/system.md'
    }
,{
        'pattern_name': 'summarize_paper',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/summarize_paper/system.md'
    }
,{
        'pattern_name': 'summarize_prompt',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/summarize_prompt/system.md'
    }
,{
        'pattern_name': 'summarize_pull-requests',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/summarize_pull-requests/system.md'
    }
,{
        'pattern_name': 'summarize_rpg_session',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/summarize_rpg_session/system.md'
    }
,{
        'pattern_name': 'to_flashcards',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/to_flashcards/system.md'
    }
,{
        'pattern_name': 'transcribe_minutes',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/transcribe_minutes/system.md'
    }
,{
        'pattern_name': 'tweet',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/tweet/system.md'
    }
,{
        'pattern_name': 'write_essay',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/write_essay/system.md'
    }
,{
        'pattern_name': 'write_hackerone_report',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/write_hackerone_report/system.md'
    }
,{
        'pattern_name': 'write_latex',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/write_latex/system.md'
    }
,{
        'pattern_name': 'write_micro_essay',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/write_micro_essay/system.md'
    }
,{
        'pattern_name': 'write_nuclei_template_rule',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/write_nuclei_template_rule/system.md'
    }
,{
        'pattern_name': 'write_pull-request',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/write_pull-request/system.md'
    }
,{
        'pattern_name': 'write_semgrep_rule',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/write_semgrep_rule/system.md'
    }


]

# List to store all scraped data
all_scraped_data = []

# Scrape each pattern
for pattern in patterns_to_scrape:
    scraped_content = scrape_system_md(
        url=pattern['url'],
        pattern_name=pattern['pattern_name']
    )
    all_scraped_data.append(scraped_content)

# Save the combined output to a JSON file
output_filename = 'scraped_fabric_patterns.json'
with open(output_filename, 'w') as json_file:
    json.dump(all_scraped_data, json_file, indent=4)

print(f"Data has been scraped and saved to '{output_filename}'")