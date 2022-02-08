def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    me = []
    friend = []
    me.append(yourLeft)
    me.append(yourRight)
    friend.append(friendsLeft)
    friend.append(friendsRight)
    if min(me) == min(friend) and max(me) == max(friend):
        return(True)
    else:
        return(False)
