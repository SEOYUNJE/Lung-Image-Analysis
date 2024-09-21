## xLSTM: Extended Long Short-Term Memory

Attempts to scale LSTMs to billions of parameters using the latest techniques from modern LLMs and mitigating common limitations of LSTMs.

To enable LSTMs the ability to revise storage decisions, they introduce exponential gating and a new memory mixing mechanism (termed sLSTM).

To enhance the storage capacities of LSTMs, they add a matrix memory and a covariance update rule (termed mLSTM).

Both the sLSTM and xLSTM cells stabilize their exponential gates using the same technique.

These extensions lead to xLSTM blocks that are residually stacked into the final xLSTM architecture.

Compared to Transformers, xLSTMs have a linear computation and constant memory complexity concerning the sequence length.

The xLSTM architecture is shown to be efficient at handling different aspects of long context problems.

![](https://www.googleapis.com/download/storage/v1/b/kaggle-forum-message-attachments/o/inbox%2F19186184%2F553d10b765685f9c6cdb43fb3ce05cc4%2F20240509_105022.jpg?generation=1715265245484790&alt=media)
