def recive(ref, name ,ts, mode):
    mode_list = ["Recived","Sent"]
    mail = ref.child(mode_list[mode]).child(name).child(ts).get()
    return mail