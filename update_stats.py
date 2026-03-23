import urllib.request
import json
import re

USERNAME = "amitpadhan525"
README_PATH = "README.md"

def fetch_hackerrank_data(username):
    profile_url = f"https://www.hackerrank.com/rest/contests/master/hackers/{username}/profile"
    badges_url = f"https://www.hackerrank.com/rest/hackers/{username}/badges"
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Fetch profile
    req = urllib.request.Request(profile_url, headers=headers)
    with urllib.request.urlopen(req) as response:
        profile_data = json.loads(response.read().decode())['model']
        
    # Fetch badges
    req_badges = urllib.request.Request(badges_url, headers=headers)
    with urllib.request.urlopen(req_badges) as response:
        badges_data = json.loads(response.read().decode())['models']
        
    return profile_data, badges_data

def update_readme(profile_data, badges_data):
    title = profile_data.get('title', 'Unknown')
    title = title.replace('<', '&lt;').replace('>', '&gt;')
    # We will preserve the HTML tags for sup like <sup>N</sup> in Title if it's there
    title = title.replace('O(&lt;sup&gt;N&lt;/sup&gt;)', 'O(<sup>N</sup>)') # Edge case for their exact title
    
    if badges_data:
        best_badge = max(badges_data, key=lambda x: x.get('current_points', 0))
        badge_name = best_badge.get('badge_name', 'Unknown')
        stars = best_badge.get('stars', 0)
        points = int(best_badge.get('current_points', 0))
        level = best_badge.get('level', 0)
        stars_str = '⭐' * stars
    else:
        badge_name, stars, stars_str, points, level = "None", 0, "", 0, 0
        
    html = f"""  <p>
    <b>Title:</b> {title} | <b>{badge_name} Badge:</b> {stars} Stars {stars_str} | <b>Points:</b> {points} | <b>Level:</b> {level}
  </p>"""

    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Matches everything between <!-- hackerrank_start --> and <!-- hackerrank_end -->
    pattern = r'(<!-- hackerrank_start -->\n).*?(\n\s*<!-- hackerrank_end -->)'
    replaced = re.sub(pattern, rf'\g<1>{html}\g<2>', content, flags=re.DOTALL)
    
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(replaced)

if __name__ == "__main__":
    print(f"Fetching HackerRank data for {USERNAME}...")
    try:
        p_data, b_data = fetch_hackerrank_data(USERNAME)
        print("Updating README.md...")
        update_readme(p_data, b_data)
        print("Success! README.md has been updated with your latest stats.")
    except Exception as e:
        print(f"Failed to update README.md: {e}")
