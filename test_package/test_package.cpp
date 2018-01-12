#include <concurrentqueue/concurrentqueue.h>

int main()
{
    moodycamel::ConcurrentQueue<int> q;
    for (int i = 0; i != 123; ++i)
        q.enqueue(i);
    int item;
    for (int i = 0; i != 123; ++i) 
    {
        q.try_dequeue(item);
        assert(item == i);
    }
}
