import sys
import os
sys.path.append('./lib/')

from myo import Myo
from device_listener import DeviceListener
from pose_type import PoseType

class WavePoseListener(DeviceListener):
	def on_pose(self, pose):
		pose_type = PoseType(pose)

		if pose_type.name == 'WAVE_OUT':
			os.system('xdotool key Right')
		elif pose_type.name == 'WAVE_IN':
			os.system('xdotool key Left')

def main():
    print('Start MyoPresenter for Linux')

    listener = WavePoseListener()
    myo = Myo()

    try:
        myo.connect()
        myo.add_listener(listener)

        while True:
            myo.run()

    except KeyboardInterrupt:
        pass
    except ValueError as ex:
        print(ex)
    finally:
        myo.safely_disconnect()
        print('Finished.')

if __name__ == '__main__':
    main()
