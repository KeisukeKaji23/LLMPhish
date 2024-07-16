import json
import os

from funcs.judge_website import judge_website

from funcs.retreat_visual_data import retreat_visual_data

root_dir = os.path.dirname(os.path.abspath(__file__))

retreat_visual_data(
    root_dir + "/screenshots", root_dir + "/site_visual_dict.json", type="other"
)


def main(role, website_type, upper_limit):
    if website_type == "phishing" or website_type == "benign":
        with open("contet.json", "r") as f:
            json_conetnt = json.load(f)
            content = json_conetnt[role]
            with open(
                f"/home/keisukekaji/my-study/dataset/{website_type}/site_visual_dict.json",
                "r",
            ) as f:
                site_visual_dict = json.load(f)
                model_name = "gpt-4-turbo"
                judge_website(
                    content,
                    site_visual_dict,
                    model_name,
                    f"/home/keisukekaji/my-study/result/{website_type}/{role}_{website_type}_result.json",
                    upper_limit,
                )
    else:
        with open("other_content.json", "r") as f:
            json_conetnt = json.load(f)
            content = json_conetnt[role]
            with open(
                f"{root_dir}/site_visual_dict.json",
                "r",
            ) as f:
                site_visual_dict = json.load(f)
                model_name = "gpt-4-turbo"
                judge_website(
                    content,
                    website_type,
                    site_visual_dict,
                    model_name,
                    f"{root_dir}/results/{role}_{website_type}_result.json",
                    upper_limit,
                )


main("expert", "other", 100)
main("common_person", "other", 100)
main("common_person_with_knowledge", "other", 100)
