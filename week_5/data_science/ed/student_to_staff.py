# for loading files with nested data
import json


def main():
    # load the data
    ed_data = json.load(open('ed.json'))
    # print(type(ed_data)) list

    n_teacher_posts = 0
    # loop over each post in the list
    for post in ed_data:
        # get the role of the author of the post
        role_str = post['user']['role']
        # if the post came from a teacher
        if role_str == 'tutor' or role_str == 'admin':
            # increase the count
            n_teacher_posts += 1

    # show the fraction of posts from teachers
    n_posts = len(ed_data)
    print(n_teacher_posts / n_posts)


if __name__ == '__main__':
    main()
