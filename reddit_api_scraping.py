def get_submission_vote_count(reddit, submission_id):
    from math import ceil
    from numpy import nan as np_nan

    try:
        submission = reddit.submission(id=submission_id)
        submission_score = submission.score
        submission_upvote_ratio = submission.upvote_ratio
    except:
        return [np_nan, np_nan]  # Return NaN if the submission is hidden or inaccessible for some reason

    # Calculate the number of upvotes and downvotes
    if submission_upvote_ratio == 1:
        return [submission_score, 0]
    if submission_upvote_ratio == 0.5:
        return [submission_score / 2, submission_score / 2]

    downvotes = submission_score * (submission_upvote_ratio - 1) / (-2 * submission_upvote_ratio + 1)
    upvotes = -submission_upvote_ratio * downvotes / (submission_upvote_ratio - 1)

    return [ceil(upvotes), ceil(downvotes)]


def get_submission_flair(reddit, submission_id):
    try:
        submission = reddit.submission(id=submission_id)
        submission_flair = submission.link_flair_text.lower()
    except:
        return None  # Return NaN if the submission is hidden or inaccessible for some reason

    return submission_flair


def get_comment_score(reddit, comment_id):
    from numpy import nan as np_nan

    try:
        comment = reddit.comment(id=comment_id)
        comment_score = comment.score
    except:
        return np_nan  # Return NaN if the comment is hidden or inaccessible for some reason

    return comment_score


def scrape_post_votes(reddit, ids): 
    ups = []
    downs = []
    for id in ids:
        [up, down] = get_submission_vote_count(reddit, id)
        print(f"ID: {id} - Upvotes: {up}, Downvotes: {down}")
        ups.append(up)
        downs.append(down)

    return [ups, downs]


def scrape_post_flairs(reddit, ids): 
    flairs = []
    for id in ids:
        flair = get_submission_flair(reddit, id)
        print(f"ID: {id} - Flair: {flair}")
        flairs.append(flair)
    
    return flairs


def scrape_post_vote_and_flair(reddit, path, fname, save_path):
    import pandas as pd

    # Read the csv file containing the submission ids for the posts that I have voted
    post_votes = pd.read_csv(path + fname)

    # Get votes
    print("Getting vote counts for posts that I have voted on...")
    ups, downs = scrape_post_votes(reddit, post_votes["id"])
    # Add the upvotes and downvotes to the dataframe
    post_votes["Upvotes"] = ups
    post_votes["Downvotes"] = downs

    # Get flairs
    print("Getting flairs for posts that I have voted on...")
    flairs = scrape_post_flairs(reddit, post_votes["id"])
    # Add the flairs to the dataframe
    post_votes["Flair"] = flairs

    # Save the dataframe to a csv file
    post_votes.to_csv(save_path + fname, index=False)
    print(f"Saved the vote counts to {save_path + fname}")


def scrape_comment_votes(reddit, path, fname, save_path):
    import pandas as pd

    # Read the csv file containing the submission ids for the comments that I have voted
    comment_votes = pd.read_csv(path + fname)
    scores = []
    for id in comment_votes["id"]:
        score = get_comment_score(reddit, id)
        print(f"ID: {id} - Score: {score}")
        scores.append(score)

    # Add the scores to the dataframe
    comment_votes["Score"] = scores

    # Save the dataframe to a csv file
    comment_votes.to_csv(save_path + fname, index=False)
    print(f"Saved the vote counts to {save_path + fname}")


def get_sub_flairs(reddit, path, fname, save_path):
    import pandas as pd

    # Read the csv file containing the subreddit names
    subreddits_df = pd.read_csv(path + fname)

    # Add flairs column to the dataframe
    subreddits_df["Flairs"] = None

    # Get the flairs for each subreddit
    for sub_name in subreddits_df["subreddit"]:
        sub = reddit.subreddit(sub_name)
        
        try:
            flairs = []
            for f in sub.flair.link_templates:
                flairs.append(f["text"].lower())
            flairs = ", ".join(flairs)
        except:
            flairs = None
            
        # Add the flairs to the dataframe
        subreddits_df.loc[subreddits_df["subreddit"] == sub_name, "Flairs"] = flairs

    
    # Save the dataframe to the csv file
    subreddits_df.to_csv(save_path + fname, index=False)
    print(f"Saved the sub flairs to {save_path + fname}")


def main():
    import pandas as pd
    import praw
    import os
    from dotenv import load_dotenv
    # Load environment variables from .env file
    load_dotenv()

    # Get Reddit client
    # Authenticate with Reddit using password flow
    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        password=os.getenv("REDDIT_PASSWORD"),
        username=os.getenv("REDDIT_USERNAME"),
        user_agent="script:myRedditDataCollecterBot:v1.0.0 by u/personalScraper",
    )

    raw_data_path = "./data/raw_data/"
    save_path = "./data/scrapped_data/"

    scrape_post_vote_and_flair(reddit, raw_data_path, "post_votes.csv", save_path=save_path)

    print("Getting vote counts for comments that I have voted on...")
    scrape_comment_votes(reddit, raw_data_path, "comment_votes.csv", save_path=save_path)

    scrape_post_vote_and_flair(reddit, raw_data_path, "post_headers.csv", save_path=save_path)

    print("Getting vote counts for the comments that I have created...")
    scrape_comment_votes(reddit, raw_data_path, "comment_headers.csv", save_path=save_path)

    print("Getting flairs for the subreddits...")
    get_sub_flairs(reddit, raw_data_path, "subscribed_subreddits.csv", save_path=save_path)

    
    # Combine annotated tags with scrapped data
    annotated_data = pd.read_csv(raw_data_path + "Tag_Responses.csv")
    scrapped_data = pd.read_csv(save_path + "subscribed_subreddits.csv")
    scrapped_data["Tags"] = None  # Add a new column for the tags

    # Read the tags for each sub
    for col in annotated_data.columns[1:]:  # Skip the first column which is the timestamp
        sub_name = col.split(" ")[0][2:]
        tags = annotated_data[col].map(lambda x: x.split(", ")).explode().value_counts()
        accepted_tags = tags[tags >= tags.mean()].sort_values().index.to_list()[:3]

        scrapped_data.loc[scrapped_data["subreddit"] == sub_name, "Tags"] = ", ".join(accepted_tags)

    # Save the dataframe to the csv file
    scrapped_data.to_csv(save_path + "subscribed_subreddits.csv", index=False)


if __name__ == "__main__":
    main()