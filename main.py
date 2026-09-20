from stages.stage1_video_sampling import run_stage1
from stages.stage2_object_detection import run_stage2
from stages.stage3_visual_embedding import run_stage3
from stages.stage4_similarity_search import run_stage4
from stages.stage5_temporal_grouping import run_stage5
from stages.stage6_ai_verification import run_stage6


def main():

    # Stage 1
    run_stage1()

    # Stage 2
    run_stage2()

    # Stage 3
    run_stage3()

    # Stage 4
    run_stage4()

    # Stage 5
    run_stage5()

    # Stage 6
    run_stage6()


if __name__ == "__main__":
    main()