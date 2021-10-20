from .models import HouseType, Houses, Community, CommunityType
import random
import string

all_communities = Community.objects.all()
test_community = Community.objects.get(pk=1)


def geninsert(comm):
    total_houses = 0
    #Generator
    if comm.communitytype.housetype.is_block:
        if comm.communitytype.housetype.is_flat:
            #With Flats
            #get number of blocks
            block_count = comm.communitytype.housetype.block_count
            b_num = 0
            for block in range(1,block_count+1):
                b_num += 1
                b_code = f"BL{b_num}"
                #get number of flats
                flat_count = comm.communitytype.housetype.flat_count
                f_num = 0
                f_code = None
                for flat in range(1, flat_count+1):
                    f_num += 1
                    f_code = f"FT{f_num}"
                    h_code = f"{comm.commcode}/{b_code}/{f_code}"
                    h_status = 0

                    house = Houses.objects.create(community=comm, housecode=h_code, housestatus=h_status)
                    if Houses.objects.filter(housecode=h_code).exists():
                        pass
                    else:
                        house.save()
                        total_houses += 1
        else:
            #Without Flats
            #get number of blocks
            block_count = comm.communitytype.housetype.block_count
            b_num = 0
            for block in range(1,block_count+1):
                b_num += 1
                b_code = f"BL{b_num}"
                #Randomly Choose Letters for adding to code
                char1 = random.choice(string.ascii_uppercase)
                char2 = random.choice(string.ascii_lowercase)
                char3 = random.choice(string.ascii_letters)
                char4 = random.choice(123456789)
                ##########################
                h_code = f"{comm.commcode}/{char1}{char2}{char3}{char4}/{b_code}"
                h_status = 0
                house = Houses.objects.create(community=comm, housecode=h_code, housestatus=h_status)
                if Houses.objects.filter(housecode=h_code).exists():
                    pass
                else:
                    house.save()
                    total_houses += 1