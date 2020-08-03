from multiprocessing import Process
import time

def test(x):
    # for i in range(4):

    #     print(x)

    #     time.sleep(1)
    return x;

if __name__=='__main__':
    p=Process(target=test,args=(10,))
    p.start()

    time.sleep(3)

    if p.is_alive():
        print("error")
        p.terminate()
        p.join()

    else:
        print(p)
        print('works')
        
    print('finished-testing')