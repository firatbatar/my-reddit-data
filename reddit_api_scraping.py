def get_reddit_client():
    import praw
    import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()

    # Authenticate with Reddit using password flow
    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        password=os.getenv("REDDIT_PASSWORD"),
        username=os.getenv("REDDIT_USERNAME"),
        user_agent="testscript by u/personalScraper",
    )

    return reddit  # Return the Reddit client


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


def get_comment_score(reddit, comment_id):
    from numpy import nan as np_nan

    try:
        comment = reddit.comment(id=comment_id)
        comment_score = comment.score
    except:
        return np_nan  # Return NaN if the comment is hidden or inaccessible for some reason

    return comment_score


def scrape_post_votes(reddit, file_path):
    import pandas as pd

    # Read the csv file containing the submission ids for the posts that I have voted
    post_votes = pd.read_csv(file_path)
    ups = []
    downs = []
    for id in post_votes["id"]:
        [up, down] = get_submission_vote_count(reddit, id)
        print(f"ID: {id} - Upvotes: {up}, Downvotes: {down}")
        ups.append(up)
        downs.append(down)

    # Add the upvotes and downvotes to the dataframe
    post_votes["Upvotes"] = ups
    post_votes["Downvotes"] = downs

    # Save the dataframe to a csv file
    post_votes.to_csv(file_path, index=False)
    print(f"Saved the vote counts to {file_path}")


def scrape_comment_votes(reddit, file_path):
    import pandas as pd

    # Read the csv file containing the submission ids for the comments that I have voted
    comment_votes = pd.read_csv(file_path)
    scores = []
    for id in comment_votes["id"]:
        score = get_comment_score(reddit, id)
        print(f"ID: {id} - Score: {score}")
        scores.append(score)

    # Add the scores to the dataframe
    comment_votes["Score"] = scores

    # Save the dataframe to a csv file
    comment_votes.to_csv(file_path, index=False)
    print(f"Saved the vote counts to {file_path}")


def main():
    import pandas as pd

    # Get Reddit client
    reddit = get_reddit_client()
    data_path = "./data/"

    print("Getting vote counts for posts that I have voted on...")
    scrape_post_votes(reddit, data_path + "post_votes.csv")


    print("Getting vote counts for comments that I have voted on...")
    scrape_comment_votes(reddit, data_path + "comment_votes.csv")


    print("Getting vote counts for the posts that I have created...")
    scrape_post_votes(reddit, data_path + "post_headers.csv")


    print("Getting vote counts for the comments that I have created...")
    scrape_comment_votes(reddit, data_path + "comment_headers.csv")


if __name__ == "__main__":
    main()